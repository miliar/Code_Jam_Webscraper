#include<stdio.h>
#include<iostream>    
using namespace std;

struct node{
   int x;
   struct node* next;
};        
                       

void enqueue(struct node** head,struct node** end,int data){                
   struct node* tmp;
   tmp=new struct node;
   tmp->x=data;
   tmp->next=NULL;
   if(*head==NULL){
      *head=tmp;
      *end=tmp;
   }else{
      (*end)->next=tmp;
      *end=(*end)->next;
   }
}

void display(struct node *head)           //Displaying the elements
{
     struct node* tmp;
     tmp=head;
     while(tmp!=NULL){                    //Iterating tmp to reach the last element
       cout<<tmp->x;;
        tmp=tmp->next;
     }
     cout<<"\n";
}

void dequeue(struct node **head)
{
struct node* temp;
while(*head!=NULL){
temp=(*head)->next;
delete *head;
*head=temp;
}
}

int add(struct node* head)
{
int sum=0;
while(head!=NULL){
sum+=head->x;
head=head->next;
}
return sum;
}
int main()
{
freopen("C-small-attempt0(2).in","r",stdin);
freopen("output","w",stdout);
struct node *head=NULL,*end=NULL,*temp=NULL,*temp1=NULL;
int r,k,n,p,a,tmp,m,out;
cin>>p;
for(int i=0;i<p;i++)
{
out=0;
cin>>r>>k>>n;
for(int j=0;j<n;j++){
cin>>a;
enqueue(&head,&end,a);
}
int sum=0;
for(int m=0;m<r;m++){
temp=head;
while(sum<=k && temp!=NULL){
sum+=temp->x;
tmp=temp->x;
temp1=temp;
temp=temp->next;
}
if(add(head)>k)
sum-=tmp;
temp=temp1;
temp1=head;
head=temp;
end->next=temp1;
while(temp1->next!=temp)
temp1=temp1->next;
end=temp1;
end->next=NULL;
out+=sum;
sum=0;
}
cout<<"Case #"<<i+1<<": "<<out<<endl;
dequeue(&head);
}
return 0;
}




      
