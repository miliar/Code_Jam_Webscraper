#include<fstream>
#include<vector>
using namespace std;

struct Action
{
	int pos;
	char color;
};

int main(){

	ifstream fin;

	fin.open("input.txt");

	int num,numaction;
	Action tempa;
	fin>>num;
	vector<Action> list;
	ofstream fout;
	fout.open("output.txt");
	
	for(int i=0;i<num;i++)
	{
		fin>>numaction;
		
		

		int ocurrent=1;
		int bcurrent=1;
		for(int j=0;j<numaction; j++)
		{	
			fin>>tempa.color;
			fin>>tempa.pos;
			list.push_back(tempa);
		}
		int minact(0),lasto(0),lastb(0);
		int bi(0),oi(0),mini(0);
		while(numaction>mini){
		while((bi<numaction)&&(list[bi].color!='B')) bi++;
		while((oi<numaction)&&(list[oi].color!='O')) oi++;
		if(oi<bi)
			mini=oi;
		else
			mini=bi;

		while(mini <bi){
		
			if(abs(list[oi].pos-ocurrent)>(minact-lasto))
			minact =abs(list[oi].pos-ocurrent)+lasto;
			minact++;
			lasto=minact;
			ocurrent=list[oi].pos;
			do{oi++;}while((oi<numaction)&&(list[oi].color!='O'));
			if(oi>bi)
				mini=bi;
			else
				mini=oi;	
		}

		while((mini ==bi)&&(bi<list.size())){
		
			if(abs(list[bi].pos-bcurrent)>(minact-lastb))
			minact =abs(list[bi].pos-bcurrent)+lastb;
			minact++;
			lastb=minact;
			bcurrent=list[bi].pos;
			do{bi++;}while((bi<numaction)&&(list[bi].color!='B'));
			if(bi>oi)
				mini=oi;
			else
				mini=bi;

		
		}


		}

		fout<<"Case #"<<i+1<<": "<<minact<<endl;
		list.clear();
	}

	


}