#include<iostream>
using namespace std;

void magicka();

int main(){
	int T;		//Total number of test cases
//	cout<<"Enter total number of test cases\t";
	cin>>T;
	for (int i=1;i<=T;i++){
		cout<<"\nCase #"<<i<<": ";
		magicka();
	}
	return 0;
}

void magicka(){

	int C;		//Total number of cominations
//	cout<<"Enter total number of combining base letters";
	cin>>C;
	char comb[C][3];
	int i,j,k,l, flag=0;			//loop counters and flag
	for(i=0;i<C;i++){
//		cout<<"Enter 2 base elements followed by their combination";
		cin>>comb[i][0]>>comb[i][1]>>comb[i][2];
	}
/*//Input check
for(i=0;i<C;i++){
	for(j=0;j<=2;j++)
		cout<<comb[i][j]<<" ";
	cout<<endl;
}
*/
	int D;		//Total number of Destructing elements
//	cout<<"Enter total number of destructing elements";
	cin>>D;
	char dest[D][2];
	for(i=0;i<D;i++){
//		cout<<"Enter 2 base elements that are opposed to each other";
		cin>>dest[i][0]>>dest[i][1];
	}

	int N;		//Total number of elements
//	cout<<"Enter number of elements in final string";
	cin>>N;
	char string[N];
	for(i=0;i<N;i++){
//		cout<<"Enter the elements";
		cin>>string[i];	
	}
	char invoke[N];
	int base[N];			//array to store position of base elements in invoked array
	int n=0,b=0;			//counters for invoke and base arrays
	for(i=0;i<N;i++){
//		if(string[i]=='Q'||string[i]=='W'||string[i]=='E'||string[i]=='R'||string[i]=='A'||string[i]=='S'||string[i]=='D'||string[i]=='F'){
		if(n>0){
			//base element combination	
			if(base[b-1]==(n-1)){
				for(j=0;j<C;j++){
					for(k=0;k<2;k++){
						if(string[i]==comb[j][k]){
							if(k==0){
								if(invoke[n-1]==comb[j][1]){
									invoke[n-1]=comb[j][2];
									flag=1;
																							
									//n--;
								}
							}							
							else if(k==1){
								if(invoke[n-1]==comb[j][0]){
									invoke[n-1]=comb[j][2];
									flag=1;//n--;
								}				
							}
							if(flag==1)
								break;
						}
					}//for k
					if(flag==1)
						break;
				}//for j
				if(flag==1){
					flag=0;
					continue;			//continue i loop
				}
			}//if invoke
			
			//element invoke
			invoke[n]=string[i];
			base[b]=n;
			n++;b++;
		
			//base element destruction
			
			for(j=0;j<D;j++){
				for(k=0;k<2;k++){
					if(invoke[n-1]==dest[j][k]){
						if(k==0){
							for(l=b-2;l>=0;l--){
								if(dest[j][1]==invoke[base[l]]){
									n=0;
									b=0;
									break;			//break l loop
								}
							}	
						}
						else if(k==1){
							for(l=b-2;l>=0;l--){
								if(dest[j][0]==invoke[base[l]]){
									n=0;
									b=0;
									break;			//break l loop
								}
							}//for l
						
						}//if k
					}//if invoke
				}// for k
			}//for j
			continue;
		}//if n
		else if(n==0){
			invoke[n]=string[i];
			base[b]=n;
			n++;b++;
		}
//		}//if string
/*//would never be executed
		else {
			invoke[n]=string[i];		
			n++;	
		}
*/
/*//ITERATION CHECK
cout<<"\ni="<<i<<"\nn="<<n<<"\nb="<<b<<"\n[";
for(int x=0;x<n-1;x++)
	cout<<invoke[x]<<", ";
cout<<invoke[n-1]<<"]";
*/
	
	}//for i
			
	if(n>0){
	cout<<"[";
	for(i=0;i<n-1;i++)
		cout<<invoke[i]<<", ";
	cout<<invoke[n-1]<<"]";}
	else
		cout<<"[]";
}

