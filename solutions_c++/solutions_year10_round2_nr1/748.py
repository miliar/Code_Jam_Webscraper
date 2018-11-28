#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <conio.h>
//#include<>
using namespace std;

int min(int a, int b)
{
  return a<b?a:b;  
    
};

int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("A-small-attempt1(3).in",ios::in);
    out.open("ap.out",ios::out);
    int t,M,N,T,result,i,j,k,ind;
    bool found;
    in >> T;
    vector <string> tc(0),ex(0),dirs(0);
    string ts;
    for (t=1;t<=T;t++)
    {
        tc.clear();
//        tc.reset();
  //      ex.reset();
        ex.clear();
        in>>N>>M;
        for (i=0;i<N;i++) 
        {
              in>>ts;
              ex.push_back(ts);
        };
        for (i=0;i<M;i++) 
        {
              in>>ts;
              tc.push_back(ts);
        };
        for (i=0;i<M;i++) for (j=i+1;j<M;j++) if (tc[i]>tc[j])
        {
            ts=tc[i];
            tc[i]=tc[j];
            tc[j]=ts;           
        };
//                for (i=0;i<tc.size();i++) out<< tc[i]<<"\n";
        for (i=0;i<N;i++) for (j=i+1;j<N;j++) if (ex[i]>ex[j])
        {
            ts=ex[i];
            ex[i]=ex[j];
            ex[j]=ts;           
        };    
        result=0;    
        dirs.clear();
        dirs.push_back("/");
        ind=1;
        for (i=0;i<M;i++)
        {
            ts="";
//            out<<"\n"<<i<<" "<<j<<" "<<ts<<"=ts\n";            
            for (j=0;(j<dirs[ind-1].size())&&(j<tc[i].size());j++) 
            {if (tc[i][j]==dirs[ind-1][j])
                {
                    ts+=tc[i][j];
                }
                else break;
            };
//            out<<"\n"<<i<<" "<<j<<" "<<ts<<"=ts\n";
            j=ts.size();
            if ((ts.size()==dirs[ind-1].size())&&(ts.size()>1)) {j++;ts+="/";}
            else
            {
                        while (ts[j-1]!='/') j--;
                        j++;
                        ts=tc[i].substr(0,j);
            };
            do
            {
                
                 while ((j<tc[i].size())&&(tc[i][j]!='/'))
                 {
                    ts+=tc[i][j];
                    j++;       
                 };

                found=false;
                for (k=0;k<N;k++) if (ex[k]==ts) {found=true; break;};
                if (!found) result++;
                dirs.push_back(ts);
                ind++;
                ts+="/";
                j++;
                
            } while (j<tc[i].size());

        };               
        out<<"Case #"<<t<<": "<<result<<"\n";
//        for (i=0;i<dirs.size();i++) out<< dirs[i]<<"\n";
    };

    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}
