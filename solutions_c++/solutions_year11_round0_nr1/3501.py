#include <iostream>

using namespace std;

int main(){
	int cases, buttons, blue, orange, turns, bmoves, omoves, pos, temp;
	char color;
	cin>>cases;
	for (int z=1; z<=cases; z++){
		cin>>buttons;
		blue=1;
		orange=1;
		turns=0;
		bmoves=0;
		omoves=0;
		for (int j=0; j<buttons; j++){
			cin>>color;
			cin>>pos;
			if (color=='O'){
				temp=abs(pos-orange);
				if (omoves>temp){
					bmoves++;
					turns++;
				}
				else {
					temp-=omoves;
					temp++;
					bmoves+=temp;
					turns+=temp;
				}
				orange=pos;
				omoves=0;
			}
			else {
				temp=abs(pos-blue);
				if (bmoves>temp){
					omoves++;
					turns++;
				}
				else {
					temp-=bmoves;
					temp++;
					omoves+=temp;
					turns+=temp;
				}
				blue=pos;
				bmoves=0;
			}
		}
		cout<<"Case #"<<z<<": "<<turns<<endl;
	}
	return 0;
}
