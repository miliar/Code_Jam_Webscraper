#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    long m=0,N=0,i,j,k=0,r=0,n=0,pos=0,cap=0,st=0,flg=0;

    ifstream f;
    ofstream of;
    of.open("E:\\Users\\DEVARADHAN\\Desktop\\1st.txt");
    f.open("E:\\Users\\DEVARADHAN\\Desktop\\A-small-attempt5.in");
    f>>N;
    int set[100];
    int cost=0;
    for(m=0;m<N;m++)
        {

        f>>r>>k>>n;
        cost=0;
        for(i=0;i<n;i++)
          f>>set[i];
        pos=0;

        for(j=0;j<r;j++)
        {
            st=pos;
            while(cap<k)
            {
                if(cap+set[pos]<=k)
                {

                    cap+=set[pos];
                    pos=(pos+1)%n;
                    if(pos==st)
                      break;
                }
                else
                  break;

            }
            cost+=cap;
            cap=0;
        }
        of<<"\nCase #"<<m+1<<": "<<cost;
        }
    return 0;

}
