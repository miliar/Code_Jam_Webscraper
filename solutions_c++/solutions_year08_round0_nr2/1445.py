#include <iostream>
#include <stdio.h>
using namespace std;

char timetemp[6]="00:00";
typedef struct {
	int s;
	int t;
	bool A;
}interval;
interval train[220];
interval *tmptrain;
int sCmp(const void* a, const void* b)
{
	return (((interval*)a)->s)-(((interval*)b)->s);
}
int parse(char *t)
{
    short HH=(t[0]-'0')*10+t[1]-'0';
    short MM=(t[3]-'0')*10+t[4]-'0';
    return HH*60+MM;
}
int main()
{
    int i,j,n,na,nb,turn;
    char temp[100];
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>turn;
        cin>>na>>nb;
        for(j=0;j<na+nb;j++)
        {
            cin>>temp;
            train[j].s=parse(temp);
            cin>>temp; 
            train[j].t=parse(temp)+turn;
            train[j].A=(j<na);
        }    
        qsort((void *)train,na+nb,sizeof(interval),sCmp);
        short removeout=0,end,countA=0,countB=0;
        end=train[0].t;
        bool removed[220];
        bool swtch;
        for(j=0;j<na+nb;j++)
            removed[j]=false;
        while(removeout<na+nb)
        {
            for(j=0;removed[j];j++);
            swtch=train[j].A;
            end=train[j].t;
            if(swtch)
                countA++;
            else
                countB++;    
            removed[j]=true;
            removeout++;
            for(j++;j<na+nb;j++)
            {
                if(removed[j])
                    continue;
                if(swtch!=train[j].A&&train[j].s>=end){
                    swtch=train[j].A;
                    end=train[j].t;
                    removed[j]=true;
                    removeout++;    
                }
            }
        }
        printf("Case #%d: %d %d\n",i+1,countA,countB);    
    }    
    return 0;
}
