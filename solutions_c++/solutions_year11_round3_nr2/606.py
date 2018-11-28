#include <iostream>


using namespace std;



int main() {
int T;
long long L,t,N,C,a;
cin>>T;
for(int temp_case=1;temp_case<=T;temp_case++) {
cin>>L>>t>>N>>C;
int Distances[N];
for(int i=0;i<C;i++) {
cin>>a;
for(int k=0;(k+i)<N;k=k+C)
Distances[k+i] = a;
}
int sum=0;
for(int i=0;i<N;i++) {
sum+=Distances[i];
}
int ans=sum*2;
int Distances_2[N];
for(int i=0;i<N;i++) {
Distances_2[i]=Distances[i]; }
int temp_sum=0;
for(int i=0;i<N;i++) {
temp_sum+=Distances[i];
if((temp_sum)>(t/2)) {
Distances[i] = temp_sum-(t/2);   
break;         
}
Distances[i] = 0;
}
for(int a=0;a<N;a++) {
for(int i=0;i<(N-1);i++) {
if(Distances_2[i]<Distances_2[i+1]) {
int temp=Distances_2[i+1];
Distances_2[i+1] = Distances_2[i];
Distances_2[i] = temp;
temp=Distances[i+1];
Distances[i+1] = Distances[i];
Distances[i] = temp;               
}      
}
}
for(int a=0;a<N;a++) {
for(int i=0;i<(N-1);i++) {
if(Distances[i]<Distances[i+1]) {
int temp=Distances[i+1];
Distances[i+1] = Distances[i];
Distances[i] = temp;               
}      
}
}
int diff=0;
for(int i=0;i<N && L>0;i++) {
diff+=Distances[i];
L--;
}
ans = ans-diff;
cout<<"Case #"<<temp_case<<": "<<ans<<endl;
}
return 0;
}

