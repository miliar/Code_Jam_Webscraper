#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
using namespace std;

fstream fin, fout;
int N;
int T, NA, NB;
const int A_TO_B = 0;
const int B_TO_A = 1;
const int cityA = 0;
const int cityB = 1;

class Time
{
private:

       int _hours;
       int _minutes;
public:
       Time()
       {

           _hours = 0;
           _minutes = 0;
       }       
       int getHours() const
       {
           return _hours;
       }
       
       int getMinutes() const
       {
           return _minutes;
       }
       
       void setHours(int inValue)
       {
            _hours = inValue;
       }
       
       void setMinutes(int inValue)
       {
            _minutes = inValue;
       }
       
       bool operator< (const Time & right) const
       {
           
            if (_hours < right._hours)
               return true;
               
            if (_hours == right._hours)
               return _minutes <= right._minutes;
               
            return false;
       }
       
       Time operator+ (int m) const
       {
            Time res;

            int minutes = _minutes + m;

            res._minutes = minutes % 60;
            res._hours = _hours + (minutes / 60);

            
            return res;
       }
       
       friend istream& operator>>(istream& istr, Time &time)
       {
              char s[6];
              
              istr >> s;
              
              time.setHours((s[0]-'0')*10 + s[1]-'0');
              time.setMinutes((s[3]-'0')*10 + s[4]-'0');
              
              return istr;
              
       }
       
       void print() const
       {
            cout << _hours << ":" << _minutes <<"\n";
       }
       
};
      

class Course
{
private:
       Time _begin;
       Time _end;
       int _direction;

public:
       Time getBegin() const
       {
           return _begin;
       }
       
       Time getEnd() const
       {
           return _end;
       }
       
       void setBegin(Time inValue)
       {
            _begin = inValue;
       }
       
       void setEnd(Time inValue)
       {
            _end = inValue;
       }
       
       int getDirection() const
       {
           return _direction;
       }
       
       void setDirection(int inValue)
       {
            _direction = inValue;
       }
       
       bool operator< (const Course & right) const
       {
            if (_begin < right._begin)
               return true;

            if (right._begin < _begin)
               return false;
               
            return _end < right._end;
            
       }
       
       friend istream& operator>>(istream& istr, Course &course)
       {
              istr >> course._begin;
              istr >> course._end;
              return istr;
       }
       
       void print() const
       {
            _begin.print();
            _end.print();
            cout << "\n";
       }
       
};

class Bus
{
private:
      int _startFrom;
      int _position;
      Time _canStartAt;

public:
       Bus(int startFrom = 0, int position = 0, Time canStartAt = Time())
       {
               _startFrom = startFrom;
               _position = position;
               _canStartAt = canStartAt;
       }
       
       int getStartFrom() const
       {
           return _startFrom;
       }
            
       void setStartFrom(int inValue)
       {
            _startFrom = inValue;
       }
       
       int getPosition() const
       {
           return _position;
       }
       
       void setPosition(int inValue)
       {
            _position = inValue;
       }
       
       Time getCanStartAt() const
       {
            return _canStartAt;
       }
       
       void setCanStartAt(Time inValue)
       {
            _canStartAt = inValue;
       }
       
       void print() const
       {
            cout << "Bus: from ";

            if (_startFrom == cityA)
               cout << "A";
            else
               cout << "B";
            

            cout << ", position ";
            if (_position == cityA)
               cout << "A";
            else
               cout << "B";
               
            cout << " , time: ";
            _canStartAt.print();
               
       }

           
};

Course courses[200];
Bus buses[200];
int countBuses = 0;
int countCourses = 0;
int countBusesFromA = 0;
int countBusesFromB = 0;

void sortCourses(Course * courses, int countCourses)
{
     for (int i = 0; i < countCourses-1; i++)
     {
         int minIndex = i;
         
         for (int j = i+1; j < countCourses; j++)
         {
             if (courses[j] < courses[minIndex])
                minIndex = j;
         }
         
         if (minIndex != i)
            swap(courses[i], courses[minIndex]);
     }
     
}

int findMinBusIndex(int direction)
{
    int index = -1;
    for (int i = 0; i < countBuses; i++)
        if (buses[i].getPosition() == direction)
        {
              if (index == -1)
                 index = i;
              
              if (buses[i].getCanStartAt() < buses[index].getCanStartAt())
                 index = i;
            
        }
    
    return index;
    
}

void solve()
{
     
    countBuses = 0;
    countBusesFromA = 0;
    countBusesFromB = 0;

    countCourses = NA + NB;
    
    sortCourses(courses, NA + NB);
   
    int i = 0;
    
    while (i < countCourses)
    {
          //courses[i].print();
          
          int dir = courses[i].getDirection();          
          int minIndex = findMinBusIndex(dir);
          
          if (minIndex == -1 || countBuses == 0 || !(buses[minIndex].getCanStartAt() < courses[i].getBegin()))
          {
               buses[countBuses].setCanStartAt(courses[i].getEnd() + T);
               buses[countBuses].setStartFrom(courses[i].getDirection());
               buses[countBuses].setPosition(1-courses[i].getDirection());

             // buses[countBuses].print();
               
               countBuses++;

          }
          else
          {
               buses[minIndex].setCanStartAt(courses[i].getEnd() + T);
               buses[minIndex].setPosition(1-courses[i].getDirection());
          }
          
         
          
          i++;
    }
     
}

int main()
{
    fin.open("input.txt", ios::in);
    fout.open("output.txt", ios::out);
    
    fin >> N;
    
    int k = 0;
           
    while (k < N)
    {
          k++;
          fin >> T;
          fin >> NA >> NB;
          int i, j;
          
          for (i = 0; i < NA; i++)
          {
              fin >> courses[i];
              courses[i].setDirection(A_TO_B);
          }
          
          for (j = i; j < NA+NB; j++)
          {
              fin >> courses[j];
              courses[j].setDirection(B_TO_A);
          }
          
          solve();
          
          countBusesFromA = 0;
          countBusesFromB = 0;
          for (i = 0; i < countBuses; i++)
          {
              if (buses[i].getStartFrom() == cityA)
                 countBusesFromA++;
          }
          countBusesFromB = countBuses - countBusesFromA;
          
          
          //fout << resetiosflags(ios::fixed) << setprecision(1);
          fout << "Case #" << k <<": " << countBusesFromA << " " << countBusesFromB;
          fout << "\n";
          
    }

   // system("pause");
    
    return 0;
    
 
    
}
