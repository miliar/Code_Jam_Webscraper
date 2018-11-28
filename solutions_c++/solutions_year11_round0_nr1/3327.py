#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]){

	ifstream fp;
	fp.open(argv[1]);
	if(fp.is_open()){
		char color;
		int numcase;
		int numbut;
		int step;
		fp>>numcase;
		for(int i = 0 ; i < numcase;i++){
			fp>>numbut;
			int o=1;
			int b=1;
			int eb=0;
			int eo=0;
			int count=0;
			for(int j = 0 ; j < numbut;j++){
				fp>>color>>step;
				if(color == 'O'){
					if(o==step || eo >= abs(o-step)){
						count++;//press button
					}
					else{
						//walk and press button
						count += (abs(o-step)-eo+1);
						eb += (abs(o-step)-eo);
					}
					o = step;
					eb++;//press button
					eo = 0;
				}
				else{

					if( b == step || eb >= abs(b-step)){
						count++;
					}
					else{
						count += (abs(b-step) - eb + 1);
						eo+=(abs(b-step) - eb);
					}
					b=step;
					eo++;
					eb = 0;
				}
				if(0){
					cout<<color<<" "<<step<<endl;
					cout<<"extra O: "<<eo<<endl;
					cout<<"extra B: "<<eb<<endl;
					cout<<count<<endl;
					cout<<"============"<<endl;
				}
			}
			cout<<"Case #"<<i+1<<": "<<count<<endl;
		
		}

	
	}


	return 0;
}
