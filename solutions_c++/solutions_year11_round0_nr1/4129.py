#include<cstdio>
int blue[1000], orange[1000], q[1000];
int main(){
    int t,tt,n,i,j,k,y,bluel,orangel,time,blueat,orangeat;
    char x[3];
    freopen("A-large.in", "r", stdin);
    freopen("A-large.txt", "w", stdout);
    scanf("%d",&tt);
    for(t=1;t<=tt;t++){
        bluel=0;
        orangel=0;
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%s",x);
            scanf("%d",&y);
            if(x[0]=='B'){
                blue[bluel++]=y;
                q[i]=0;
            }else{
                orange[orangel++]=y;
                q[i]=1;
            }
        }
        i=0;
        j=0;
        k=0;
        blueat=1;
        orangeat=1;
        for(time=0;k<n;time++){
            int bluemove=0;
            int orangemove=0;
            if(blueat<blue[i]){blueat++;bluemove=1;}
            else if(blueat>blue[i]){blueat--;bluemove=1;}
            if(orangeat<orange[j]){orangeat++;orangemove=1;}
            else if(orangeat>orange[j]){orangeat--;orangemove=1;}
            if(q[k]==0&&blueat==blue[i]&&!bluemove){
                k++; i++;
            }else if(q[k]==1&&orangeat==orange[j]&&!orangemove){
                k++; j++;
            }
        }
        printf("Case #%d: %d\n",t,time);
    }
}
