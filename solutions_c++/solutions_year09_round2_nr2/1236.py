#include<iostream>
#include<vector>
#include<string>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<fstream>
using namespace std;
vector<string> v;
int main()
{
    ofstream f("out1.in");
    int t,i,j,k,m,temp,flag,temp1,val,l,count;
    string out="";
    char max,min;

    cin>>t;
    v.resize(t);
    for(i=0;i<t;i++)
    cin>>v[i];
    for(i=0;i<t;i++)
    {
       count=0;
        out=v[i];
        k=0;
        while(k<=v[i].length()-2 && v[i].size()!=1)
        {

            max=v[i][v[i].length()-2-k];
            flag=0;
        for(j=v[i].length()-2-k,temp=j;j<v[i].length();j++)
        {
            if(v[i].at(j)>v[i].at(temp) && (flag==0 || v[i].at(j)<max))
            {
               max=v[i][j];
               val=j;
               flag=1;
               }
            }

        if(max!=v[i].at(temp))
        {

            v[i].insert(temp,1,v[i][val]);
            v[i].erase(val+1,1);



            for(j=temp+1;j<v[i].length();j++)
            {
                min=v[i][j];
                temp1=j;
                for(m=j+1;m<v[i].length();m++)
                {
                    if(v[i][m]<min)
                    {
                    min=v[i][m];
                    temp1=m;
                    }
                    }
                v[i].insert(j,1,v[i][temp1]);
                v[i].erase(temp1+1,1);

                }
                break;
            }
            else
            k++;
        }
        if(v[i]==out)
        {
            for(j=0;j<v[i].length();j++)
            {
                if(v[i][j]=='0')
                {
                    count++;
                    v[i].erase(j,1);
                    j--;
                    }
                }

            for(j=0;j<v[i].length();j++)
            {
            flag=0;
            for(m=0;m<v[i].length();m++)
            {

                   if(flag==0 )
                   {

                       min=v[i][m];
                       temp1=m;
                       flag==1;

                       }
                    else
                    {
                        if(v[i][m]<min )
                        min=v[i][m];
                        temp1=m;
                    }
                        }

                v[i].insert(j,1,v[i][temp1]);
                v[i].erase(temp1+1,1);
            }


           /* for(j=1;j<v[i].length();j++)
            {
                min='\0';

                for(m=j;m<v[i].length();m++)
                {
                    if((v[i][m]<min || min=='\0') )
                    {


                            min=v[i][m];
                            temp1=m;

                    }
                    }

            }*/

        // if(v[i].length()%2==0)
        // l=v[i].length()/2;
        // else
        // l=(v[i].length()+1)/2;
        for(m=0;m<=count;m++)
        {
           v[i].insert(1,1,'0');
           l++;
            }
    }
        f<<"Case #"<<i+1<<": "<<v[i]<<endl;
        }
    return 0;
    }
