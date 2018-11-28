#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<vector>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("A-large.in",ios::in);

    ofstream fout;
    fout.open("A-large.out",ios::out);

    int no_cases,N,M;
    vector<string> p1,p;
    string::iterator z;

    string s,s1;

    fin>>no_cases;

    bool b;
    int call = 0,l,j;

    for(int c = 0; c < no_cases; c++)
    {
        fin>>N>>M;
        call = 0;
        p1.clear();

        for(int i = 0; i<N;i++)
        {
            fin>>s;
            p1.push_back(s);
        }
        sort(p1.begin(),p1.end() );

        for(int i = 0; i < M;i++)
        {
            fin>>s;

            b = binary_search(p1.begin(),p1.end(),s);
    j = s.length();
            while( b != 1&&s.length() >0)
            {


                call++;
                p1.push_back(s);
                sort(p1.begin(),p1.end());
                l = 0;
                s1 = s;
                for(; s[j] != '/' ; j--)
                {
                      l++;
                      s.erase(j,1);
                }
                s.erase(j,1);
                cout<<j<<" ";
                //s.erase(j,l-1);
                //s1 = s;
                //for(int k = 0; k < p1.length();k++)
                  //  cout<<p1[k]<<"\n";
                b = binary_search(p1.begin(),p1.end(),s);
                //cout<<s<<" "<<b<<" "<<"\n";
            }
            //cout<<"done";

        }

        fout<<"Case #"<<c+1<<": "<<call<<"\n";


    }
}
