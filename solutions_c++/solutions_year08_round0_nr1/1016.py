#include <fstream.h>
#include <string.h>
const char *out_file="out.txt";
int main()
{
	char in_file[256];
	cout<<"Please enter the name of the input file:"<<endl;
	cin.getline(in_file,256);
	ifstream input;
	input.open(in_file);
	if (! input){
		cout<<"Can not open the file!"<<endl;
		return 1;
	}
	ofstream output;
	output.open(out_file);
	if (! output){
		cout<<"Can not open the file!"<<endl;
		return 1;
	}
	int case_num;
	input>>case_num;
	int *engines_num;
	engines_num=new int[case_num];
	for (int i=0;i<case_num;i++){
		input>>engines_num[i];
		char **engines;
		engines=new char *[engines_num[i]];
        for (int j=0;j<engines_num[i];j++) engines[j]=new char[256];
		input.getline(engines[0],256);
		for (j=0;j<engines_num[i];j++) input.getline(engines[j],256);
		int querys_num;
		input>>querys_num;
		int *querys;
		querys=new int[querys_num];
		char q_temp[256];
		input.getline(q_temp,256);
		for (j=0;j<querys_num;j++){
			input.getline(q_temp,256);
			for (int k=0;k<engines_num[i];k++)
				if (strcmp(engines[k],q_temp)==0) { querys[j]=k; break;}
		}
		int count=0;
		int index=0;
		int *switch_test;
		switch_test=new int[engines_num[i]];
		for (j=0;j<engines_num[i];j++) switch_test[j]=0;
		while (index<querys_num){
			switch_test[querys[index]]=1;
			bool test=true;
			for (int k=0;k<engines_num[i];k++) if (switch_test[k]==0) { test=false; break; }
			if (test){
				count++;
				for (int kk=0;kk<engines_num[i];kk++) switch_test[kk]=0;
			}else index++;
		}
		output<<"Case #"<<i+1<<": "<<count<<endl;
	}
	input.close();
	output.close();
	return 0;
}
