#include<iostream>
#include<cmath>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
#define oo 1.0e9
typedef unsigned long long i64;
int main()
{
    int test_cases=0,case_num=1,L,N,c,iter,k,max,store;
    int dist[1000];
    int find;
    i64 t,hours,total;
    string line;
    ifstream myinput; ofstream myoutput;
    myinput.open("B-small-attempt1.in");
    myoutput.open("output.txt");
    if(myinput.is_open())
    {
        getline(myinput,line);
        for(int i=0;i<line.size();i++)
        {test_cases=test_cases*10+int(line[i])-48;}
        while(test_cases--)
        {
            getline(myinput,line);
            iter=0;
            L=0;
            while(line[iter]!=' ')
            {
                L=10*L+int(line[iter])-48;
                iter++;
            }
            iter++;
            t=0;
            while(line[iter]!=' ')
            {
                t=10*t+int(line[iter])-48;
                iter++;
            }
            
            iter++;
            N=0;
            while(line[iter]!=' ')
            {
                N=10*N+int(line[iter])-48;
                iter++;
            }
            
            iter++;
            c=0;
            while(line[iter]!=' ')
            {
                c=10*c+int(line[iter])-48;
                iter++;
            }
            
            iter++;
            
            for(int i=0;i<c;i++)
            {dist[i]=0;}
            k=0;
            while(iter<line.size())
            {
                if(line[iter]==' ') k++;
                else{
                    dist[k]=10*dist[k]+int(line[iter])-48;
                }
                iter++;
            }
            for(int i=c;i<N;i++)
            { dist[i]=dist[i%c];}
            hours=0;
            for(int i=0;i<c;i++)
            {
                hours+=2*dist[i];
            }
            hours=hours*(N/c);
            for(int i=0;i<N%c;i++)
            {
                hours+=2*dist[i];
            }
            if(L==0 || t>hours){
                myoutput<<"Case #"<<case_num<<": "<<hours<<endl;
            }
            else if(L>=1){
                cout<<"hours"<<hours<<endl;
                find=0;
                total=0;
                max=0;
                while(find<N)
                {
                    if(total<t){ total+=2*dist[find%c]; find++;}
                    else break;
                }
                if(total==t){
                    cout<<"=hours"<<hours<<endl;
            
                    store=find;
                    for(int i=find;i<N;i++)
                    {
                        if(dist[i%c]>max){max=dist[i%c]; store=i;}
                    }
                    hours-=max;
                    if(L==1){myoutput<<"Case #"<<case_num<<": "<<hours<<endl;}
                    else{
                        cout<<"in"<<endl;
                        dist[store]=0;
                        L--;
                        while(L)
                        {
                            store=(find+1);
                            max=0;
                            for(int i=find;i<N;i++)
                            {
                            if(dist[i%c]>max){max=dist[i%c]; store=i;}
                            }
                            hours-=max;
                            if(L==1){myoutput<<"Case #"<<case_num<<": "<<hours<<endl;}
                            dist[store]=0;
                            L--;
                        }
                    }       
                }
                else{
                    store=(find-1);
                    cout<<"total"<<total<<endl;
                    total-=2*dist[(find-1)%c];
                    
                    cout<<"total"<<total<<endl;
                    max=dist[(find-1)%c]-(t-total)/2;
                    cout<<"max"<<max<<endl;
                    for(int i=find;i<find+c && i<N;i++)
                    {
                        if(dist[i%c]>max){max=dist[i%c]; store=i;}
                    }
                    cout<<"max"<<max<<endl;
                    
                    hours-=max;
                    cout<<"hrs"<<hours<<endl;
                    if(L==1){myoutput<<"Case #"<<case_num<<": "<<hours<<endl;}
                    else{
                        cout<<"in"<<endl;
                        cout<<"hours"<<hours<<endl;
            
                        dist[store]=0;
                        L--;
                        while(L)
                        {
                            store=(find+1);
                            max=0;
                            for(int i=find;i<N;i++)
                            {
                            if(dist[i%c]>max){max=dist[i%c]; store=i;}
                            }
                            hours-=max;
                            if(L==1){myoutput<<"Case #"<<case_num<<": "<<hours<<endl;}
                            dist[store]=0;
                            L--;
                        }
                    }
                }
            }
            case_num++;
        }
    }
    myoutput.close();
    system("pause");
    return 0;
}

