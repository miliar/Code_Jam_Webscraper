#include <iostream>
#include <string>

using namespace std;

int main(){
	int cases,button,count;
	string color;
	int Bnext[101],Onext[101],Anext[101];
	bool type[101];
		

	cin >>cases;
	
	int Ocur,Bcur,Opos,Bpos;	

	for(int s=0;s<cases;s++){
		cin >>button;
		Ocur=0;
		Bcur=0;
		Opos=1;
		Bpos=1;
		for(int r=0;r<button;r++){
			cin >>color >> count;
			Anext[r]=count;
			if(color=="O"){
				type[r]=false;
				Onext[Ocur]=count;
				Ocur++;
			}else if (color=="B"){
				type[r]=true;
				Bnext[Bcur]=count;
				Bcur++;
			}					
		}
		count=0;
		Ocur = Bcur =0;
		for(int m=0;m<button;m++){
			while(true){
				count++;
				if(type[m]==false){
					if(Bpos>Bnext[Bcur]){
						Bpos--;
					}else if(Bpos<Bnext[Bcur]){
						Bpos++;
					}
					if(Opos>Onext[Ocur]){
						Opos--;
					}else if(Opos<Onext[Ocur]){
						Opos++;
					}else if(Opos==Onext[Ocur]){
						Ocur++;
						break;
					}	
				}else if(type[m]==true){
					if(Opos>Onext[Ocur]){
                                                Opos--;
                                        }else if(Opos<Onext[Ocur]){
                                                Opos++;
                                        }
					if(Bpos>Bnext[Bcur]){
                                                Bpos--;
                                        }else if(Bpos<Bnext[Bcur]){
                                                Bpos++;
                                        }else if(Bpos==Bnext[Bcur]){
						Bcur++;
						break;
					}

					
				}

			}	

		}
		cout <<"Case #"<<s+1<<": "<< count<<endl;	
	}
}
