#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
int abs(int i){
	if(i > 0) return i;
	else return (-1*i);
}

int main(){
	ifstream in;
	in.open("./input1");
	ofstream out;
	out.open("./output1");
//	bool OButt[100],BButt[100];
	int i,T,N,ncase,Obegin,Bbegin,Otime,Btime,time,Opos,Bpos;
	char tmp;
	in>>T;
	for(ncase=1;ncase<=T;ncase++){
		Obegin = Bbegin = Opos = Bpos = 1;
		Otime = Btime = time = 0;
//		for(i=0;i<100;i++){
//			OButt[i]=BButt[i]=false;
//		}
		in>>N;
		in>>tmp;
		if(tmp == 'O'){
			in>>Opos;
			Otime = abs((Opos-Obegin))+1;
			Obegin = Opos;
//			OButt[Opos-1] = true;
		}
		else{
			in>>Bpos;
			Btime = abs((Bpos-Bbegin))+1;
			Bbegin = Bpos;
//			BButt[Bpos-1] = true;
		}
		N--;
		while(N){
			if(tmp == 'O'){
				while(N){
					in>>tmp;
					if(tmp == 'B'){
						in>>Bpos;
						N--;
//						if(!BButt[Bpos-1]){
                                        		Btime += abs((Bpos-Bbegin));
                                        		Bbegin = Bpos;
//							BButt[Bpos-1] = true;
							break;
//						}
//						continue;
					}
					in>>Opos;
//					if(!OButt[Opos-1]){
						Otime+=abs((Opos-Obegin))+1;
                                		Obegin = Opos;
//						OButt[Opos-1] = true;
//					}
					N--;
				}
				if(Otime >= Btime){
					time+=Otime;
					Btime=1;
					Otime=0;
				}
				else{
					time+=Btime;
					Otime=Otime-Btime;
					Btime=1;
				}
				continue;
			}
			if(tmp == 'B'){
                                while(N){
					in>>tmp;
					if(tmp == 'O'){
						in>>Opos;
						N--;
//                                                if(!OButt[Opos-1]){
                                                        Otime += abs((Opos-Obegin));
                                                        Obegin = Opos;
//                                                        OButt[Opos-1] = true;
                                                        break;
//                                                }
//                                                continue;
					}
                                        in>>Bpos;
//					if(!BButt[Bpos-1]){
                                        	Btime+=abs((Bpos-Bbegin))+1;
                                        	Bbegin = Bpos;
//						BButt[Bpos-1] = true;
//					}
                                        N--;
                                }
                                if(Btime >= Otime){
					time+=Btime;
					Otime = 1;
					Btime = 0;
				}
                                else{
					time+=Otime;
					Btime = Btime-Otime;
					Otime = 1;
				}
                                continue;
                        }
		}
		if((tmp == 'O' && Otime > 0) || (tmp == 'B' && Btime > 0)) time++;
		out<<"Case #"<<ncase<<": "<<time<<endl;
	}
	in.close();
	out.close();
	return 0;
}
