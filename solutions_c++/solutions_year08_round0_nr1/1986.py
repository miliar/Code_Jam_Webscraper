
#include <cstdio>
#include <iostream>
#include <vector>
#include <conio.h>
   
using namespace std;

bool one_is_zero(vector <int>);
int where(vector <string>, string);
    
int main()
{
    int no_of_engines, no_of_q, no_of_cases;
    int answer;
    char name1[101];
    string name;
    int forp=1;
    int d;
    scanf("%d", &no_of_cases);
    d = no_of_cases;
    // cout<<no_of_cases;
    while(no_of_cases--)
    {                
        vector <string> a;
        vector <int> b;
        answer = 0;
        scanf("%d", &no_of_engines);
     //   cout<<"e"<<no_of_engines;
        int n = no_of_engines;
        while(no_of_engines--)
        {
            scanf(" %[^\n]", name1);
            name = name1;
           // cout<<name;
         //   getch();
            a.push_back(name);
            b.push_back(0);
        }       
        scanf("%d", &no_of_q); 
      //  cout<<"q"<<no_of_q;   
        //n = no_of_q;
       // cout<<n;
        while(no_of_q--)
        { //printf("here");
            scanf(" %[^\n]", name1);
            name = name1;
            if((one_is_zero(b))&& b[where(a, name)] == 0)
            {
                //cout<<"z";
                //cout<<name;
                answer++;
                for(int i=0;i<b.size();i++)
                {
                    b[i] = 0;                  
                }
                b[where(a,name)] = 1;
            }
            else
            {
                //cout<<"n"<<name;
                b[where(a,name)] = 1;
             //   cout<<"current senario";
             //   for(int i=0;i<b.size();i++)
             //   {
             //       cout<<"\n";
             //       cout<<b[i];
             //   }
             //   cout<<"\n";
            }
        }
        cout<<"Case #"<<forp++<<": ";
        cout<<answer;
        if(forp <= d)
                   cout<<"\n";
    }
}

bool one_is_zero(vector <int>a)
{
    bool f=0;
    int c=0;
    for(int i=0;i<a.size();i++)
    {
        if(a[i]==0)
                   c++;
    }
    if(c==1)
        return 1;
    else
        return 0;
}

int where(vector <string> buff, string q)
{
    for(int i=0;i<buff.size();i++)
    {
        if(buff[i]==q)
            return i;
    }
            return -1;    
}
