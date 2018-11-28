#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int testcases,numOfGooglers,spTrip,p;
bool isSurprisingTripletPossible(int num,int div)
{
    if( num == 0 || num == 1)
        return false;
    int reminder = num%3;
    if(reminder == 0 || reminder == 1)
    {
        if((div+1)>10)
            return false;
    }
    else if(reminder == 2)
    {
        if((div+2)>10)
            return false;
    }
    else
        return true;
}
bool isPliesInTriplet(int num, int div, int& presentSpTrip)
{
    bool isSpPossible = isSurprisingTripletPossible(num,div);
    int reminder = num%3;
    if(div+1 == p)
    {
        if(reminder ==1|| reminder == 2)
        {
            return true;
        }
        else if(isSpPossible&&(presentSpTrip< spTrip))
        {
            presentSpTrip++;
            return true;
        }

        else
            return false;
    }
    else if(((div+2)==p)&&isSurprisingTripletPossible(num,div)&&(presentSpTrip< spTrip))
    {
        if(reminder ==0|| reminder == 1)
        {
            return false;
        }
        else
        {
            presentSpTrip++;
            return true;
        }
    }
}
int main()
{
    cin >> testcases;
    for(int i =0; i< testcases; i++)
    {
         cin >> numOfGooglers >> spTrip >> p;
         vector <int> scores;
         int tempScr;
         for(int k =0 ; k<numOfGooglers;k++)
         {
             cin >> tempScr;
             scores.push_back(tempScr);
         }

         sort(scores.begin(),scores.end());
         int num,div;
         int presentSpTrip = 0;
         int presentP =0;
         for(vector<int> ::reverse_iterator itr = scores.rbegin(); itr<scores.rend();itr++)
         {
             num = *itr;
             div = num/3;
             if((div+2)<p)
                break;
             if(div>=p)
                presentP++;
             else if(isPliesInTriplet(num,div,presentSpTrip))
                presentP++;
         }
         cout<<"Case #"<<i+1<<": "<<presentP<<endl;
    }
    return 0;
}
