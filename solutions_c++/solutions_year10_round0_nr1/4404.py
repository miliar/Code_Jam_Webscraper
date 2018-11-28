#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int n,k,m,N,i,j;
    ifstream f;
    ofstream of;
    of.open("E:\\Users\\DEVARADHAN\\Desktop\\1st.txt");
    f.open("E:\\Users\\DEVARADHAN\\Desktop\\A-small-attempt5.in");
    f>>N;
    bool *cur,*state;
    cur=new bool[35];
    state=new bool[35];
    for(m=0;m<N;m++)
        {
            f>>n;
            f>>k;

        for(i=0;i<35;i++)
        {
            state[i]=false;
            cur[i]=false;
        }
        cur[0]=true;
        for(i=0;i<k;i++)
        {
            for (j=0;j<n;j++)
            {
                if(cur[j]==true)
                {
                    state[j]=!state[j];

                }
                else
                  break;

            }
            for (j=0;j<n;j++)
            {
                if(state[j]==true&&cur[j]==true)
                {
                    cur[j+1]=true;

                }
                else
                    cur[j+1]=false;
                //    cout<<i<<" cur["<<j<<"]="<<cur[j]<<" state["<<j<<"]="<<state[j]<<endl;

            }
        }


        if(cur[n]==true)
            of<<"\nCase #"<<(m+1)<<": ON";
        else
            of<<"\nCase #"<<(m+1)<<": OFF";



        }

    return 0;

}
