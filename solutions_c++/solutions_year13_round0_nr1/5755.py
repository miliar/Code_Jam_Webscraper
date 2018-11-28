#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(){
	int n;
	cin>>n;
	int z = 1;
	while(z <= n){
		string table[4];
		cin.ignore();
		for(int i=0;i < 4;i++)
			getline(cin, table[i]);
		bool notcomplete = false;
		char diag0 = table[0][0];
		char diag1 = table[0][3];
		bool d0,d1,set0,set1;
		char pivot0,pivot1;
		d0 = d1 = true;
		int r0, r1;
		r0 = r1 = 0;
		if (diag0 == 'T')
				r0 = 1;
		if (diag1 == 'T')
				r1 = 1;
		int minCount0 = 0;
		int minCount1 = 0;
		for(int i=0;i < 4;i++){
			if(table[i][i] == '.' || table[i][4-i-1] == '.'){
					notcomplete = true;
			}
			if(diag0 != '.'){
				minCount0++;
				if(!r0 && (diag0 == table[i][i] || table[i][i] == 'T'))
					d0 &= true;
				else if(r0 && table[i][i]!='.'){
					diag0 = table[i][i];
					r0 = 0;
				} else {
					d0 = false;
				}
			} else {
				d0 = false;
			}

			if(diag1 != '.'){
				minCount1++;
				if(!r1 && (diag1 == table[i][4-i-1] || table[i][4-i-1] == 'T'))
					d1 &= true;
				else if(r1 && table[i][4-i-1]!='.'){
					diag1 = table[i][4-i-1];
					r1 = 0;
				} else {
					d1 = false;
				}
			} else {
				d1 = false;
			}
			pivot0 = table[i][0];
			pivot1 = table[0][i];
			int replace0, replace1;
			replace0 = replace1 = 0;
			if (pivot0 == 'T')
				replace0 = 1;
			if (pivot1 == 'T')
				replace1 = 1;
			set0 = true;
			set1 = true;
			for(int j=0;j < 4;j++){
				if(table[i][j] == '.' || table[j][i] == '.'){
					notcomplete = true;
				}
				if(pivot0 != '.'){
					if(!replace0 && (pivot0 == table[i][j] || table[i][j] == 'T'))
						set0 &= true;
					else if(replace0 && table[i][j]!='.'){
						pivot0 = table[i][j];
						replace0 = 0;
					} else {
						set0 = false;
					}
				} else {
					set0 = false;
				}
				if(pivot1 != '.'){
					if(!replace1 && (pivot1 == table[j][i] || table[j][i] == 'T'))
						set1 &= true;
					else if(replace1 && table[j][i]!='.'){
						pivot1 = table[j][i];
						replace1 = 0;
					} else {
						set1 = false;
					}
				} else {
					set1 = false;
				}
			}
			if (set0 || set1)
				break;
		}
		
		cout<<"Case #"<<z<<": ";
		z++;
		if(set0){
			cout<<pivot0<<" won"<<endl;
			continue;
		}
		if(set1){
			cout<<pivot1<<" won"<<endl;
			continue;
		}
		if(!notcomplete){
			cout<<"Draw"<<endl;
			continue;
		}
		if(d0){
			cout<<diag0<<" won"<<endl;
			continue;
		}
		if(d1){
			cout<<diag1<<" won"<<endl;
			continue;
		}

		cout<<"Game has not completed"<<endl;
	}
	return 0;
}