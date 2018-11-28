#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	long long int a,i,count1,count3,j,k,count_T,count_O,count_X,count2;
	char b;
	cin >> a;
	freopen ("myfile.txt","w",stdout);
	for(i=0;i<a;i++){
		count1 = 0;
		count3 = 0;
		char arr[4][4];
		count_X = 0;
		count_O = 0;
		count_T = 0;
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				cin >> b;
				if(b == '.'){
					count3 = 1;
				}
				arr[j][k] = b;
			}
		}
		for(j=0;j<4;j++){
			count_X = 0;
			count_O = 0;
			count_T = 0;
			for(k=0;k<4;k++){
				if(arr[j][k] == 'X' || arr[j][k] == 'O' || arr[j][k] == 'T'){
					if(arr[j][k] == 'X'){
						count_X++;
					}
					else if(arr[j][k] == 'O'){
						count_O++;
					}
					else if(arr[j][k] == 'T'){
						count_T++;
					}
				}
			}
		
			if(count_X == 4){
					cout << "Case #"<<(i+1) << ": X won" <<endl;
					count1 = 1;
					break; 
				}
			else if(count_O == 4){
					cout << "Case #"<<(i+1) << ": O won" <<endl;
					count1 = 1;
					break; 
				}
			
			else if((count_X + count_T) == 4){
					cout << "Case #"<<(i+1) << ": X won" <<endl;
					count1 = 1;
					break; 
			}
			else if((count_O + count_T) == 4){
					cout << "Case #"<<(i+1) << ": O won" <<endl;
					count1 = 1;
					break; 
			}
		}
		if(count1 != 1){
	
		for(k=0;k<4;k++){
				count_X = 0;
				count_O = 0;
				count_T = 0;
			for(j=0;j<4;j++){
				if(arr[j][k] == 'X' || arr[j][k] == 'O' || arr[j][k] == 'T'){
					if(arr[j][k] == 'X'){
						count_X++;
					}
					if(arr[j][k] == 'O'){
						count_O++;
					}
					if(arr[j][k] == 'T'){
						count_T++;
					}
				}
			}
			
			
				if(count_X == 4){
					cout << "Case #"<<(i+1) << ": X won" <<endl;
					count1 = 1;
					break; 
				}
				else if(count_O == 4){
					cout << "Case #"<<(i+1) << ": O won" <<endl;
					count1 = 1;
					break; 
				}
			
			else if(count_X + count_T == 4){
					cout << "Case #"<<(i+1) << ": X won" <<endl;
					count1 = 1;
					break; 
			}
			else if(count_O + count_T == 4){
					cout << "Case #"<<(i+1) << ": O won" <<endl;
					count1 = 1;
					break; 
			}
		}
	}
	if(count1 != 1){
		count_X = 0;
		count_O = 0;
		count_T = 0;
		for(j=0;j<4;j++){
			if(arr[j][j] == 'X'){
				count_X++;
			}
			if(arr[j][j] == 'O'){
				count_O++;
			}
			if(arr[j][j] == 'T'){
				count_T++;
			}
		}
			
				if(count_X == 4){
					cout << "Case #"<<(i+1) << ": X won" <<endl;
					count1 = 1;
					 
				}
				else if(count_O == 4){
					cout << "Case #"<<(i+1) << ": O won" <<endl;
					count1 = 1;
					
				}
			
			else if(count_X + count_T == 4){
					cout << "Case #"<<(i+1) << ": X won" <<endl;
					count1 = 1;
					
			}
			else if(count_O + count_T == 4){
					cout << "Case #"<<(i+1) << ": O won" <<endl;
					count1 = 1;
					
			}
		}
	
	if(count1 != 1){
		count2 = 3;
		count_X = 0;
		count_O = 0;
		count_T = 0;
		for(j=0;j<4;j++){
			if(arr[j][count2] == 'X'){
				count_X++;
			}
			if(arr[j][count2] == 'O'){
				count_O++;
			}
			if(arr[j][count2] == 'T'){
				count_T++;
			}
		count2--;
		}
			
				if(count_X == 4){
					cout << "Case #"<<(i+1) << ": X won" <<endl;
					count1 = 1;
					
				}
				else if(count_O == 4){
					cout << "Case #"<<(i+1) << ": O won" <<endl;
					count1 = 1;
					
				}
			
			else if(count_X + count_T == 4){
					cout << "Case #"<<(i+1) << ": X won" <<endl;
					count1 = 1;
					
			}
			else if(count_O + count_T == 4){
					cout << "Case #"<<(i+1) << ": O won" <<endl;
					count1 = 1;
					 
			}
		}
		if(count1 == 0 && count3 == 1){
			cout << "Case #"<<(i+1) << ": Game has not completed" <<endl;
		}
		else if(count1 == 0 && count3 == 0){
			cout << "Case #"<<(i+1) << ": Draw" <<endl;
		}
	}
	return 0;
}
	
