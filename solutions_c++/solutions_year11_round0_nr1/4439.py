#include <stdio.h>
#include <queue>

int main(){
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		std::queue<std::pair<int,int> > O,B;
		int Tc,Ct,Ni=0,Op=1,Bp=1,Ic=0;
		char Rt;
		bool Nii=false;
		scanf("%d",&Tc);
		for(int j=0;j<Tc;j++){
			scanf(" %c %d",&Rt,&Ct);
			if(Rt=='B')
				B.push(std::pair<int,int>(Ct,j));
			else
				O.push(std::pair<int,int>(Ct,j));
		}
		while(!O.empty()||!B.empty()){
			Ic++;
			if(!O.empty()){					//Orange has instructions to do
				if(Op!=O.front().first){	//if orange isnt in the right place
					if(Op>O.front().first)	//needs to move back
						Op--;
					else
						Op++;				//or forwards
				} else						//if orange is in the right place
					if(O.front().second==Ni){//is it clear to do it ?
						O.pop();
						Nii=true;
					}		
			}
			if(!B.empty()){					//blue has something to do
				if(Bp!=B.front().first){	//if blue isn't in the right place
					if(Bp>B.front().first)
						Bp--;
					else
						Bp++;
				} else						//blue is in the rihgt place
					if(B.front().second==Ni){//is it clear to do it?
						B.pop();
						Nii=true;
					}
			}
			if(Nii){ Ni++; Nii=false; }
		}
		printf("Case #%d: %d\n",i+1,Ic);
	}
}
