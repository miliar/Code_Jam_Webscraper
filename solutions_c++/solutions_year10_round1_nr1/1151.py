#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.in");
    int t;
    fin>>t;
    char **arr;
    int n,k,l,j,index;
    bool red,blue;
    for(int i=0;i<t;i++)
    {
        fin>>n>>k;
        red=false;
        blue=false;
        arr=new char*[n];
        for(j=0;j<n;j++)
        {
            arr[j]=new char[n];
            for(l=0;l<n;l++)
            {
                fin>>arr[j][l];

            }
        }
        for(j=n-1;j>=0;j--)
        {
            for(l=0;l<n;l++)
            {
                if(arr[j][l]=='.')
                {
                    for(index=l-1;index>=0;index--)
                    {
                        arr[j][index+1]=arr[j][index];
                    }
                    arr[j][0]='.';
                }
            }
        }
        int rcount=0,ccount=0;
        char cch='.',rch='.';
        for(j=0;j<n;j++)
        {
            rcount=0;
            ccount=0;
            cch='.';
            rch='.';
            for(l=0;l<n;l++)
            {

                if(arr[j][l]=='.')
                {
                    rcount=0;
                    rch='.';
                }
                else if(arr[j][l]==rch)
                {
                    rcount++;
                }
                else
                {
                    rcount=1;
                    rch=arr[j][l];
                }
                if(rcount>=k&&rch!='.')
                {
                    if(rch=='B')
                    blue=true;
                    else
                    red=true;
                }

                if(arr[l][j]=='.')
                {
                    ccount=0;
                    cch='.';
                }
                else if(arr[l][j]==cch)
                {
                    ccount++;
                }
                else
                {
                    ccount=1;
                    cch=arr[l][j];
                }
                if(ccount>=k&&cch!='.')
                {
                    if(cch=='B')
                    blue=true;
                    else
                    red=true;
                }

            }
        }
        for(j=0;j<n;j++)
        {
            rcount=0;
            cch='.';
            rch='.';
            for(l=j,index=0;l<n&&index<n;l++,index++)
            {

                if(arr[l][index]=='.')
                {
                    rcount=0;
                    rch='.';
                }
                else if(arr[l][index]==rch)
                {
                    rcount++;
                }
                else
                {
                    rcount=1;
                    rch=arr[l][index];
                }
                if(rcount>=k&&rch!='.')
                {
                    if(rch=='B')
                    blue=true;
                    else
                    red=true;
                }
            }
        }
        for(j=0;j<n;j++)
        {
            rcount=0;
            cch='.';
            rch='.';
            for(l=0,index=j;l<n&&index<n;l++,index++)
            {

                if(arr[l][index]=='.')
                {
                    rcount=0;
                    rch='.';
                }
                else if(arr[l][index]==rch)
                {
                    rcount++;
                }
                else
                {
                    rcount=1;
                    rch=arr[l][index];
                }
                if(rcount>=k&&rch!='.')
                {
                    if(rch=='B')
                    blue=true;
                    else
                    red=true;
                }
            }
        }
        for(j=0;j<n;j++)
        {
            rcount=0;
            cch='.';
            rch='.';
            for(l=j,index=n-1;l<n&&index>=0;l++,index--)
            {

                if(arr[l][index]=='.')
                {
                    rcount=0;
                    rch='.';
                }
                else if(arr[l][index]==rch)
                {
                    rcount++;
                }
                else
                {
                    rcount=1;
                    rch=arr[l][index];
                }
                if(rcount>=k&&rch!='.')
                {
                    if(rch=='B')
                    blue=true;
                    else
                    red=true;
                }
            }
        }
    for(j=0;j<n;j++)
        {
            rcount=0;
            cch='.';
            rch='.';
            for(l=n-1,index=j;l>=0&&index<n;l--,index++)
            {

                if(arr[l][index]=='.')
                {
                    rcount=0;
                    rch='.';
                }
                else if(arr[l][index]==rch)
                {
                    rcount++;
                }
                else
                {
                    rcount=1;
                    rch=arr[l][index];
                }
                if(rcount>=k&&rch!='.')
                {
                    if(rch=='B')
                    blue=true;
                    else
                    red=true;
                }
            }
        }
        if(red&&blue)
        {
            fout<<"Case #"<<i+1<<": "<<"Both"<<endl;

        }
        else if(red)
        {
            fout<<"Case #"<<i+1<<": "<<"Red"<<endl;
        }
        else if(blue)
        {
            fout<<"Case #"<<i+1<<": "<<"Blue"<<endl;
        }
        else
        {
            fout<<"Case #"<<i+1<<": "<<"Neither"<<endl;
        }
        for(j=0;j<n;j++)
        {
            delete[] arr[j];
        }
        delete[] arr;
    }

}
