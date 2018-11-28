#include<iostream.h>
#include<fstream.h>

//using namespace std;

int main(){
  int T,N;
  int Pd,Pg;
 // ifstream ifs("A-small");
  ofstream ofs("ans-a");
  cin>>T;
  for(int i=1;i<=T;++i){
    cin>>N>>Pd>>Pg;
	if(Pd==0){
		if(Pg==100)
			ofs<<"Case #"<<i<<": Broken"<<endl;
		else
			ofs<<"Case #"<<i<<": Possible"<<endl;
		continue;
	}
	int Pd1 = Pd;
	int n1 = 1;
	if((Pd/10)*10==Pd) Pd = Pd/10;
	while((Pd1/100)*100 != Pd1){
	if((Pd/5)*5==Pd){n1=n1*2;Pd=Pd/5;Pd1 = Pd1*2;}
	else if((Pd/2)*2==Pd){n1=n1*5;Pd=Pd/2;Pd1 = Pd1*5;}
	else {n1=n1*10;Pd1 = Pd1*10;}
	}
	cout<<n1<<endl;
	if(N>=n1){
		if(Pg==0)
			ofs<<"Case #"<<i<<": Broken"<<endl;
		else if(Pg == 100 && n1 != 1)
			ofs<<"Case #"<<i<<": Broken"<<endl;
		else
			ofs<<"Case #"<<i<<": Possible"<<endl;
	}
	else
		ofs<<"Case #"<<i<<": Broken"<<endl;
  }
 // ifs.close();
  ofs.close();
return 0;
  }
