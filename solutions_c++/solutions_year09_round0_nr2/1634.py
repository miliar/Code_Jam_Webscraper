#include<iostream>
#include<cmath>
#include<cstdlib>
#include<vector>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

char findsink(int i,int j,char& s, vector<vector<int> > &x, vector<vector<char> > &a)
{
    if(x[i][j]<=x[i-1][j]&&x[i][j]<=x[i][j-1]&&x[i][j]<=x[i+1][j]&&x[i][j]<=x[i][j+1])
    {
        if(a[i-1][j-1]=='0')
        {
            a[i-1][j-1]=s;
            return s++;
        }
        else return a[i-1][j-1];
    }
    else
    {
        int min=x[i-1][j],d=1;
        if(x[i][j-1]<min) {min=x[i][j-1];d=2;}
        if(x[i][j+1]<min) {min=x[i][j+1];d=3;}
        if(x[i+1][j]<min) {min=x[i+1][j];d=4;}
        switch(d)
        {
            case 1:
                return findsink(i-1,j,s,x,a);
            case 2:
                return findsink(i,j-1,s,x,a);
            case 3:
                return findsink(i,j+1,s,x,a);
            case 4:
                return findsink(i+1,j,s,x,a);
        }
    }


}

void g(ifstream& myfile)
{
    ofstream m;
    m.open ("B-large.out");
    if (myfile.is_open())
    {
        int num,c=0;
            myfile>>num;
        while(c<num)
        {
            int a,b,tmp;char s=('a');
            myfile>>a>>b;
            vector<vector<int> > t;
            for(int i=0;i<a+2;++i)
                t.push_back(vector<int>(b+2,0));
            vector<vector<char> > ans;
            for(int i=0;i<a;++i)
                ans.push_back(vector<char>(b,'0'));

            for(int i=0;i<a+2;++i)
                for(int j=0;j<b+2;++j)
                {
                    if(i==0||j==0||i==a+1||j==b+1)
                        t[i][j]=10001;
                    else
                    {
                        myfile>>tmp;
                        t[i][j]=tmp;
                    }
                }

            for(int i=1;i<a+1;++i)
                for(int j=1;j<b+1;++j)
                {
                    if(ans[i-1][j-1]=='0')
                        ans[i-1][j-1]=findsink(i,j, s, t, ans);
                }
            m<<"Case #"<<c+1<<":"<<endl;
            for(int i=0;i<a;++i)
            {
                for(int j=0;j<b-1;++j)
                    m<<ans[i][j]<<' ';
                m<<ans[i][b-1]<<endl;
            }
            ++c;
        }


        myfile.close();
        return;
    }
    else cout << "Unable to open file";
    return;
}



int main ()
{
    ifstream myfile ("B-large.in");
    //ifstream myfile ("g2.in");
    g(myfile);

    return 0;
}

