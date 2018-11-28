#include<stdio.h>
#include<stdlib.h>
typedef struct point{
    int data;
    struct point *next;
}point;

point *head,*tail,*pos,*pos2;
FILE *fp;

void createLine(int n)
{
     int i,data;
     if (head!=NULL){
        pos=head;pos2=pos;
        while(pos!=tail){
            pos=pos->next;
            free(pos2);
            pos2=pos;
        }
        free(pos);
        head=tail=pos=pos2=NULL;
     }
     for (i=0;i<n;i++){
         fscanf(fp,"%d",&data);
         if (head==NULL){
              pos=head=(point *)malloc(sizeof(point));
              pos->next=NULL;
              pos->data=data;
         }else{
              pos2=(point *)malloc(sizeof(point));
              pos2->next=NULL;
              pos2->data=data;
              pos->next=pos2;
              pos=pos->next;
         }
     }
     tail=pos;
     tail->next=head;
     pos=head;
}

int run(int r,int k,int n)
{
    int sum=0,posnum=0,i;
    while(r--){
        posnum=pos->data;i=1;
        while((posnum+pos->next->data<=k)&&(i<n)){
            posnum+=pos->next->data;
            pos=pos->next;
            i++;
        }
        pos=pos->next;
        sum+=posnum;
    }
    return sum;
}
              

int main()
{
    int t,r,k,n,sum,i;
    head=tail=pos=NULL;
    fp=fopen("3.in","r");
    fscanf(fp,"%d",&t);
    for (i=1;i<=t;i++){
        fscanf(fp,"%d%d%d",&r,&k,&n);
        createLine(n);
        printf("Case #%d: %d\n",i,run(r,k,n));
    }
    return 0;
}
