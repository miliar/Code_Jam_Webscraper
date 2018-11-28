#include<iostream>
#include<string>
using namespace std;
int main(){
int l,n,d;
cin >> l >> d >> n;
cout << l << d << n << endl;
string a[d];
string b[n];
for (int i=0; i<d;i++){
	cin >> a[i];	
}
for(int i = 0;  i< n; i++){
	cin >> b[i];
}
string temp1, temp2;
int s,t,p,count=0;
bool sach=true;
for(int i=0; i<n; i++){
	count = 0;
	for(int j =0 ; j<d;j++) {
		t = 0;
		for( int k =0 ; k<l ; k++) {
			if((b[i]).at(t) == '('){
				temp1 = (b[i]).substr(t);
				s = temp1.find(')');
				p = s+1;
				temp2 = temp1.substr(0, p);
				s = temp2.find((a[j]).at(k));
				if(s == string::npos ){
					sach= false;
					break;
					}
				else  t = t+p;	
			}
			else {if((b[i]).at(t) != ((a[j]).at(k))){
				 	sach=false;
					break;
					}
			      else t++;
			}
		}
		if(sach == true)
			count++;
		sach = true;		 			
		}
	cout << "Case #"<<i+1<<": "<< count << endl; 
	}
return 0;
}