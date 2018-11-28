#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

string convertInt(int number);

int main(int argc, char *argv[])
{
    int T;
    int t;
    int i;
    cin>>T;
    vector<int> resultvector;
   
    for(t=0;t<T;t++)
    {
        cin.ignore(256, '\n');
        int A;
        cin>>A;
        int B;
        cin>>B;
        int result=0;
        resultvector.clear();
        resultvector.push_back(0);
        for(int i=0;i<(B-A);i++)
        {       
                //cout<<"\n";
                string curr;
                string comp;
                curr = convertInt(i+A);
                //cout<<curr<<"  ";
                comp = curr;
                int ssize = curr.size();
                //cout<<ssize<<"\n";

                for(int j=1;j<ssize;j++)
                {
                    rotate(comp.rbegin(), comp.rbegin() + 1, comp.rend());
                    //cout<<comp<<"  ";
                    if(comp[0]!='0')
                    {
                           int temp=atoi(comp.c_str());
                           //cout<<temp<<"\n";
                           if(temp>=A && temp<=B && temp>(i+A) && temp!=resultvector.back())
                           {
                                      //result++;
                                      resultvector.push_back (temp);
                                      //cout<<curr<<"  "<<comp<<"\n";
                           }
                    }
                }
               // result=resultvector.size()-1;
               // cout<<resultvector.size()<<"  "<<result<<"\n";
        }
        cout<<"Case #"<<t+1<<": "<<resultvector.size()-1<<"\n";
    }        
    
    

   // system("PAUSE");
   // return EXIT_SUCCESS;
   return 0;
}

string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}
