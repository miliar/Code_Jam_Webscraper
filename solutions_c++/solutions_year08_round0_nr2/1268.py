#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;
//const int maxR = 13, maxC=9;
//const int INF = 100000;
enum Location { A , B};
class TrainTimeTable;
class TimeTable;
class Train;
class Time
{
    int hour, min;
public:
    Time(int h, int m)
    {
        hour = h;
        min = m;
    }
    Time(const Time &t)
    {
        hour = t.hour;
        min = t.min;
    }
    friend int operator<(Time &t1, Time &t2)
    {
        if(t1.hour > t2.hour)
            return 0;
        if(t1.hour == t2.hour && t1.min >= t2.min)
            return 0;
        return 1;
    }
    friend int operator<=(Time &t1, Time &t2)
    {
        if(t1.hour > t2.hour)
            return 0;
        if(t1.hour == t2.hour && t1.min > t2.min)
            return 0;
        return 1;
    }
    friend int operator ==(Time &t1, Time &t2)
    {
        if(t1.hour == t2.hour && t1.min == t2.min)
            return 1;
        return 0;
    }
    Time& operator+(int m)
    {
        Time temp(*this);
        //temp.hour = t.hour;
        //temp.min = t.min;
        temp.hour = hour + (min+m)/60;
        temp.min = (min+m)%60;
        return temp;
    }
    void display()
    {
        cout<<hour<<":"<<min;
    }
};

class Timings
{
    Time start,end;
    Location loc;
public:

    Timings():start(0,0),end(0,0)
    {
//        start= Time(0,0);
  //      end = Time(0,0);
    }
    Timings(Location l,Time s, Time e):start(s),end(e)
    {
        if(end < start)
            cout<<"\n*** ERROR ***\n";
        loc = l;
    }
    ~Timings()
    {
    }

    void display()
    {
        cout<<(loc ? "B":"A")<<" ";
        start.display();
        cout<<"   ";
        end.display();
        cout<<endl;
    }

    friend class TrainTimeTable;
    friend class TimeTable;
    friend class Train;

};

class Train
{
    Timings *timings;
    Location loc;
public:
    Train()
    {
        timings = NULL;
        loc = A;
    }
    Train(Location l, Timings tim)
    {
        timings = new Timings(tim);
        loc = l;
    }

    void set(Location l, Timings *tim)
    {
        timings->start = tim->start;
        timings->end   = tim->end;
        loc = l;
    }

    ~Train()
    {
        delete timings;
    }

    friend class TrainTimeTable;
    friend class TimeTable;

};
class TimeTable
{
    Timings *timings[201];
    int NA, NB;
    int num;
public:
    TimeTable()
    {
        NA=NB=0;
    }
    TimeTable(ifstream &fin)
    {
        char temp[11];
        int hour, min, hour1, min1;
        fin>>NA;
        fin.getline(temp,11);
        NB = atoi(temp);
        num = NA+NB;
        Location loc = A;
        for(int i=0;i<num;i++)
        {
            if(i==NA) loc = B;
            fin.getline(temp,10,':');
            hour = atoi(temp);
            //fin.get(temp[0]);
            fin.getline(temp,10,' ');
            min = atoi(temp);
            fin.getline(temp,10,':');
            hour1 = atoi(temp);
            //fin.get(temp[0]);
            fin.getline(temp,10);
            min1 = atoi(temp);
            timings[i] = new Timings(loc,Time(hour,min), Time(hour1,min1));
        }
        /*for(i=NA;i<num;i++)
        {
            fin.getline(temp,10,':');
            hour = atoi(temp);
            fin.get(temp[0]);
            fin.getline(temp,10,' ');
            min = atoi(temp);
            fin.getline(temp,10,':');
            hour = atoi(temp);
            fin.get(temp[0]);
            fin.getline(temp,10,' ');
            min = atoi(temp);
            timings[i] = new Timings(B,Time(hour,min), Time(hour1,min1));
        }*/
        //display();
        sort();
        //display();
    }

    void sort()
    {
        Timings *temp;
        for(int i=0;i<num-1;i++)
        {
            for(int j=i+1;j<num;j++)
            {
                if(timings[j]->start <timings[i]->start)
                {
                    temp = timings[j];
                    timings[j] = timings[i];
                    timings[i] = temp;    
                }
                else if(timings[j]->start  == timings[i]->start)
                {
                    if(timings[j]->end <timings[i]->end)
                    {
                    temp = timings[j];
                    timings[j] = timings[i];
                    timings[i] = temp;    
                    }
                }
            }
        }
    }

    void display()
    {
        for(int i=0;i<num;i++)
        {
            timings[i]->display();
        }
    }
    ~TimeTable()
    {
        int i=0;
        for(i=0;i<num;i++)
        {
            if(timings[i])
                delete timings[i];
            timings[i]=NULL;
        }

    }

    friend class TrainTimeTable;
};

class TrainTimeTable
{
    Train *trains[201];
    //Train *B_trains[101];
    TimeTable timeTable;
    int num_trains;
    int wait;

public:

    TrainTimeTable():timeTable()
    {
        num_trains = 0;
        wait = 0;
    }

    TrainTimeTable(int w,ifstream &fin):timeTable(fin)
    {
        num_trains = 0;
        wait = w;
    }

    void display()
    {
        timeTable.display();
    }
    
    int isAvail(Timings *t, Location loc, int pos)
    {
        int avail = -1,i=0;
        switch(loc)
        {
            case A:
                //avail = num_trains;
                for(i=0;i<num_trains;i++)
                {
                    if(trains[i]->loc == B && (trains[i]->timings->end+wait) <= t->start)
                    {
                        avail=i;
                        trains[i]->set(A,t);
                        break;
                    }
                }
/*                for(i=0; i<pos;i++)
                {
                    if(timeTable.timings[i]->loc == A)
                        avail--;
                }*/
                break;
            case B:
              //  avail = num_B;
                for(i=0;i<num_trains;i++)
                {
                    if(trains[i]->loc == A && (trains[i]->timings->end+wait) <= t->start)
                    {
                        avail=i;
                        trains[i]->set(B,t);
                        break;
                    }
                }

/*                for(i=0;i<num_trains;i++)
                {
                    if((trains[i]->timings->end+wait) <= t)
                        avail++;
                }
                for(i=0; i<pos;i++)
                {
                    if(timeTable.timings[i]->loc == B)
                        avail--;
                }*/
                break;
        }
        avail = (avail < 0)? 0:1;
        return avail;
    }

    void result()
    {
        int num_A = 0;
        int num_B = 0;
        int t_A=0,t_B=0;
        for(int i=0;i<timeTable.num;i++)
        {
            switch(timeTable.timings[i]->loc)
            {
                case A:
                    if(!isAvail(timeTable.timings[i],A,i))
                    {
                        trains[num_trains] = new Train(A,*timeTable.timings[i]);
                        num_trains++;
                        num_A++;
                    }

                break;
                case B:
                    if(!isAvail(timeTable.timings[i],B,i))
                    {
                        trains[num_trains] = new Train(B,*timeTable.timings[i]);
                        num_trains++;
                        num_B++;
                    }
                break;
            }
        }
        cout<<num_A<<" "<<num_B;
    }


    ~TrainTimeTable()
    {
        int i=0;
        for(i=0;i<num_trains;i++)
        {
            if(trains[i])
                delete trains[i];
            trains[i]=NULL;
        }
    }


};
int main(int argc, char *argv[])
{
    char filename[200]= "B-small.in";
    if(argc == 2)
    {
        strcpy(filename,argv[1]);
    }
    else if (argc>2)
    {
        cout<<"Too many arguments..."<<endl;
        cout<<"USAGE :: TrainTimeTable A-small.in\n";
        return 0;
    }
    ifstream fin(filename);
    int n=0,w=0;
    char temp[101];
    fin.getline(temp,100);
    n = atoi(temp);
    for(int i=1;i<=n;i++)
    {
        fin.getline(temp,100);
        w = atoi(temp);
        TrainTimeTable TTT(w,fin);
 //       TTT.display();
        cout<<"Case #"<< i << ": ";
        TTT.result();
        cout<<endl;
    }
    
//    system("PAUSE");
    return 0;
}
