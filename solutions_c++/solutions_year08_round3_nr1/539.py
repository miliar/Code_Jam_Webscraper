#include<iostream>
using namespace std;

int main(){
    int times;
    cin >> times;
    for(int k=0;k<times;k++)
    {
    int max_time;
    cin >>max_time;
    int keyn;
    cin >> keyn;
    int aln;
    cin >>aln;
    int fr[1000];
    for(int i=0;i<aln;i++)
    {
            cin >> fr[i];
    }
    for(int i=1;i<aln;i++)
    {
            for(int j=i;j>0;j--)
            {
                    if(fr[j]>fr[j-1])
                    {
                        int tmp=fr[j];
                        fr[j]=fr[j-1];
                        fr[j-1]=tmp;
                    }
            }
     }
    /* for(int i=0;i<aln;i++)
    {
            cout <<  fr[i];
    }*/
    //cout << endl;
    long long count=0;
    for(int i=0;i<aln;i++)
    {
            count += (fr[i]*((i/keyn)+1));
    }
    cout << "Case #"<< k+1<<": "<<count <<endl;
}
    //system("pause");
    return 0;
}