#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
 ifstream input("C:\\input.txt");
 ofstream output("C:\\output.txt");
 string searchengine[100];
 bool visited[100];
 int nooftimes;
 input>>nooftimes;
 int i;
 for(i=0;i<nooftimes;i++)
 {
         int S;
         char temp[200];
         input>>S;
         input.flush();
         int j,k,l,m;

         for(j=0;j<S;j++)
         {
                 input.getline(temp,100);
                 searchengine[j]=temp;
                 cout<<j<<":"<<temp<<"\n";
                 visited[j]=false;
         }
         int Q;
         input>>Q;
         input>>Q;
         input.getline(temp,100);
         cout<<"Q="<<Q;
         int switches=0;
         int seensearch=0;
         string current;
         cout<<S<<" "<<Q;
         cin>>j;
         cout<<"\n I am here 1";
         for(j=0;j<Q;j++)
         {
                        input.getline(temp,100);
                        current=temp;
                        cout<<"\n I am here 2";
                        for(k=0;k<S;k++)
                        {
                                        cout<<"\n I am here 3";
                                        if(current==searchengine[k] && visited[k]==false)
                                        {                                                                    {
                                         visited[k]=true;
                                         seensearch++;
                                         if(seensearch==S)
                                         {
                                                          switches++;
                                                          for(l=0;l<S;l++)
                                                          visited[l]=false;
                                         }
                                         break;
                     
                                        }
                     }
         }
         
         output<<"Case #"<<(i+1)<<" "<<switches;
}
input.close();
output.close();                     
return 0;   
}
}
