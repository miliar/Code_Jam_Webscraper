#include <iostream>
#include <fstream>
#include <stdio.h>
//#include <conio.h>
using namespace std;
int main()
{
    int total,p,num,count,surprise,cases,i,count1;
    cases=0;
    count1=1;
    fstream myfile;
    myfile.open("blah.txt");
    myfile >> cases;
    //cout << cases;
    while(cases--)
    {
            count=0;
            myfile >> num;
            myfile >> surprise;
            myfile >> p;
          //  cout<< num<<" "<<surprise<<" "<<p<<endl;
            while(num--)
            {
                        myfile >> total;
                        cout<<total<<endl;
                        if((total/3)>=p)
                        count++;
                        else
                        {
                            if((((total/3))+1==p)&&(total%3!=0))
                                count++;
                            else
                            {
                                if(((total-p)/2)+2==p)
                                {
                                                      if(surprise)
                                                      {
                                                                  surprise--;
                                                                  count++;
                                                      }
                                
                                }
                            }
                        }
            }
            ofstream fout;
            fout.open("output.txt",ios::app);
            fout<<"Case #"<<count1<<": "<<count<<"\n";
            cout<<count<<endl;
            fout.close();
            count1++;
    }
    myfile.close();
   // getch();
}
