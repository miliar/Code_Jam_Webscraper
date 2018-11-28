#include<iostream>
#include<map>

using std::map;
using std::cin;
using std::cout;

int main()
{
    int T, N, i, CNum=1;
    cin>>T;
    map<int,int> A;
    int inter=0;
    while(T--)
    {
        cin>>N;
        inter=0;
        for(i=0;i<N;i++)
        {
            int t1,t2;
            cin>>t1>>t2;
            A[t1]=t2;
        }

        for(map<int,int>::iterator iter1 = A.begin(); iter1!=A.end();iter1++)
            for(map<int,int>::iterator iter2 = A.begin(); iter2!=A.end();iter2++)
            {
                if(iter1!=iter2)
                {
                    int y1,y2,y3,y4;
                    y1=iter1->first;
                    y2=iter1->second;
                    y3=iter2->first;
                    y4=iter2->second;
                    int k=((y4-y3)- (y2-y1))*2;
                    double p=(4.00*(y1-y3))/k;
                    if(k!=0 && (p>0 && p<2))
                        inter++;
                }
            }
        A.clear();
        cout<<"Case #"<<CNum<<": "<<(inter/2)<<"\n";
        CNum++;
    }
}
