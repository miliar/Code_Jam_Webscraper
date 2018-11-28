#include<iostream>
#include<stdio.h>
#include<cmath>
#include<vector>
#include<conio.h>

using namespace std;
int distinct_pairs(int left, int right, int val, int length)
{
    vector<int> cyclicnum;
    cyclicnum.push_back(val);
    //cout<<left<<" "<<right<<" "<<val<<" "<<length;
    int total=0;
    int dupnum = val;
    int exp =length-1;
    int changednum;
    int counter =0;
    while(counter<length-1)
    {          
        changednum=0;
        int num = dupnum%10;
        dupnum = dupnum/10;
        //cout<<"num value:"<<num<< " "<<dupnum<<" "<<exp<<" "; 
        changednum = num*pow(10.0,exp)+dupnum;
        //cout<<" changed num"<<changednum<<"\n";
        if((changednum>=left) && (changednum<=right))
        {
           int flag =0;
           for(int p=0;p<cyclicnum.size();p++)
           {
                   if(changednum==cyclicnum[p])
                   flag =1;
           }
           if(flag==0)
           {
             cyclicnum.push_back(changednum);
             total++;
             }
        }
        dupnum=changednum;
        counter++;       
    }
    /*if(total>0)
    cout<<val<<" ";*/
    //cout<<"total is" <<total<<"\n";
    return total;
    
}
int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    int t;
    int left,right;
    cin>>t;
    int sum=0;
    int len;
    for(int i=0;i<t;i++)
    {
            cin>>left>>right;
            for(int j=left;j<=right;j++)
            {
                    if(j/10 ==0)
                    len=1;
                    else if(j/100 ==0)
                    len =2;
                    else if(j/1000 ==0)
                    len =3;
                    else if(j/10000 ==0)
                    len=4;
                    else if(j/10000 ==0)
                    len=5;
                    else if(j/100000 ==0)
                    len=6;
                    else if(j/1000000 ==0)
                    len =7;
                    if(len!=1)
                    sum += distinct_pairs(left,right,j,len);
            }
            cout<<"Case #"<<i+1<<": "<<sum/2<<"\n";
            sum =0;
    }
}
