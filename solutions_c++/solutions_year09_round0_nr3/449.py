#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<iomanip>
using namespace std;

string array="welcome to code jam";
const int MXSIZE=20;
const int MOD=10000;
int tot[20];
int inputsize;
int arraysize;
string input;

void display()
{
    for(int i=0;i<MXSIZE;i++)
    {
        cout<<tot[i]<<" ";
    }
    cout<<endl;
}
/*
int recurse(int iplace,int aplace, char lastchar)
{
    //base cases
    if(aplace==arraysize)return 1;
    if(iplace==inputsize)return 0;
    //if match
    int tot=0;
    if(input[iplace]==array[aplace])
    {
        tot+=recurse(iplace+1,aplace,array[aplace])+(lastchar==array[aplace]);
    }
    else
    {
        if(array[iplace]==array[aplace+1])
        {
            tot+=recurse(iplace,aplace+1,array[aplace+1]);
        }
        else
        {
            tot+=recurse(iplace+1,aplace,array[aplace]);
        }
    }
    return tot;
}
*/
/*long long memo[510][MXSIZE];
int ans;
long long recurse(int iplace,int aplace)
{
    //cout<<"iplace "<<iplace<<" aplace "<<aplace<<endl;
    //int z;
    //cin>>z;
    if(aplace==arraysize)
    {
        return 1;
    }
    if(iplace==inputsize)return 0;
    //if(memo[iplace][aplace]!=-1)return memo[iplace][aplace];
    long long tot=0;
    //decide if takeable
    if(input[iplace]==array[aplace])
    {
        tot+=recurse(iplace+1,aplace+1)%MOD;
    }
    tot+=recurse(iplace+1,aplace)%MOD;
    return memo[iplace][aplace]=tot;
}
*/
long long memo2[510][MXSIZE];
long long recurse2(int iplace,int aplace)
{
    if(aplace==-1)
    {
        //cout<<"iplace= "<<iplace<<" aplace "<<aplace<<endl;
        return 1;
    }
    if(iplace==-1)return 0;
    if(memo2[iplace][aplace]!=-1)return memo2[iplace][aplace];
    long long tot=0;
    tot+=recurse2(iplace-1,aplace)%MOD;
    if(input[iplace]==array[aplace])
    {
        tot+=recurse2(iplace-1,aplace-1);
    }
    return memo2[iplace][aplace]=tot%MOD;
}

int main()
{
    ifstream fin("C-large.in");
    ofstream fout("boutput.out");
    int ntests;
    fin>>ntests;
    getline(fin,input);
    arraysize=array.size();
    for(int ij=0;ij<ntests;ij++)
    {
        
        getline(fin,input);
        inputsize=input.size();
        for(int i=0;i<inputsize;i++)
        {
            for(int j=0;j<MXSIZE;j++)
            {
                memo2[i][j]=-1;
            }
        }
        //do brute force crap
        int actans=recurse2(inputsize-1,arraysize-1);
        fout<<"Case #"<<ij+1<<": "<<setw(4)<<setfill('0')<<actans<<endl;
    }
    cout<<"done\n";
    int z;
    cin>>z;
    return 0;
}
