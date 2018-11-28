#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int t;
	int n;
	char ch;
    int pos;
	cin>>t;
	for(int ii=0;ii<t;ii++){
		cin>>n;
		int orange_pos=1,orange_move=0,blue_pos=1,blue_move=0;
		int total_move=0;
		for(int j=0;j<n;j++){
            cin>>ch>>pos;
			if(ch=='O'){
                int diff=abs(pos-orange_pos);
            	while(total_move-orange_move<diff){
					total_move++;
				}
                total_move++;
            	orange_move=total_move;
                orange_pos=pos;
				
			} else {
            	int diff=abs(pos-blue_pos);
				while(total_move-blue_move<diff){
					total_move++;
				}
                total_move++;
            	blue_move=total_move;
                blue_pos=pos;
			}
		}
        cout<<"Case #"<<ii+1<<": "<<total_move<<endl;
    }
    return 0;
}


