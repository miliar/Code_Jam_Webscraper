#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
#define rep(X,Y) for ( int X=0; X<Y ; X++)


using namespace std;


void run(  vector<string>  &combine , vector<string> &opp,string data,int T,ofstream &fout)
{

    string master;

    master = "";
    rep( i ,data.size())
    {
        master += data[i];


            if ( master.size() >= 2)
            for ( int k=0 ;k <combine.size() ; k++)
            {
                if ((combine[k][0]== master[master.size()-1] && combine[k][1]==master[master.size()-2]) || (combine[k][1]== master[master.size()-1] && combine[k][0]==master[master.size()-2]) )
                {
                    master[master.size()-2 ] = combine[k][2];
                    master.erase(master.end()-1);
                }
            }

            if (master.size()>=2)
             for ( int k=0 ;k <opp.size() && master.size()>=2 ; k++)
            {
                char store;
                char comp;
                for ( int j=master.size()-1 ; j >= 0 ; j--)
                {
                    if ( master[j]== opp[k][0] || master[j]== opp[k][1] )
                    {
                            store = master[j];
                            if (store == opp[k][0])
                            {
                                comp =opp[k][1];
                            }
                            else
                             comp =opp[k][0];

                            for ( int l =j-1 ; l >= 0;l--)
                            {
                                if ( master[l] == comp )
                                {
                                 master.erase(master.begin(),master.end());
                                 break;
                                }

                            }
                            break;

                    }

                }

            }

   // cout<<master<<endl;
         }

         fout<<"Case #"<<T+1;
         fout<<": [";
        for ( int i=0 ; i <master.size() ; i++)
        {
            fout<<master[i];
            if ( i != master.size() -1)
            {
                fout<<", ";
            }

        }
        fout<<"]\n";

 //   cout<<master<<endl;
}
int main()
{
    ifstream fin;
    fin.open("B-large.in",ios::in);
     ofstream fout;
    fout.open("output.txt",ios::out);

    int T=0;
    int C=0,D=0,N=0;
    fin>>T;
    rep(i,T)
    {
        fin>>C;
    vector<string> combine(C);
        rep(j,C)
        {
            fin>>combine[j];
        }
    fin>>D;
    vector<string> opp(D);
        rep(k,D)
        {
            fin>>opp[k];
        }
        fin>>N;
        string data;
        fin>>data;
        run(combine,opp,data,i,fout);

    }
    fin.close();
    fout.close();

    return 0;
}
