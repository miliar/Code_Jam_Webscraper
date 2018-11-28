#include<iostream>
#include<queue>

using namespace std;


int main()
{
    
freopen("input.txt", "rt", stdin); 	freopen("output.txt", "wt", stdout);

queue<int> roller,row;
int rounds,capacity;
int left,x,n,t,oo;
int money;
int testcases;
cin>>testcases;
oo=testcases;
while((testcases--)>0){
money=0;
cin>>rounds;
cin>>capacity;
cin>>n;

while(!row.empty())
row.pop();

while(!roller.empty())
roller.pop();


for(int i=0;i<n;i++){
cin>>t;
row.push(t);
}


while((rounds--)>0)
{
left=capacity;

        while(!row.empty() && left>=(x=row.front()))
        {
        roller.push(x);
        left-=x;
        money+=x;
        row.pop();
        }

 while(!roller.empty())
 {
 row.push(roller.front());
 roller.pop();
 }

}
cout<<"Case #"<<oo-testcases<<": "<<money<<endl;
}
return 0;
}
