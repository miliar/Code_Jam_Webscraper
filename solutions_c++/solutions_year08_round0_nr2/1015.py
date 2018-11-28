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
	int turn_time;
	int na,nb;
	for (int i=0;i<case_num;i++){
		input>>turn_time>>na>>nb;
		char **table_aa=new char *[na];
		char **table_ab=new char *[na];
		for (int j=0;j<na;j++)
		{
			table_aa[j]=new char[10];
			table_ab[j]=new char[10];
			input>>table_aa[j];
			input>>table_ab[j];
		}
		char **table_bb=new char *[nb];
		char **table_ba=new char *[nb];
		for (j=0;j<nb;j++)
		{
			table_bb[j]=new char[10];
			table_ba[j]=new char[10];
			input>>table_bb[j];
			input>>table_ba[j];
		}
		int sa=na;
		int sb=nb;
		int *b=new int[nb];
		for (j=0;j<nb;j++) b[j]=1;
		for (j=0;j<na;j++){
			int m=2500;
			int k_index;
			for (int k=0;k<nb;k++){
				if (strcmp(table_aa[j],table_ba[k])!=-1 && b[k]==1){
					int m3=0; int m2=0; int m1=0; int m0=0;
					m0+=table_aa[j][4]-table_ba[k][4]; if (m0<0) { m1=-1; m0+=10; }
					m1+=table_aa[j][3]-table_ba[k][3]; if (m1<0) { m2=-1; m1+=6; }
					m2+=table_aa[j][1]-table_ba[k][1]; if (m2<0) { m3=-1; m2+=10;}
					m3+=table_aa[j][0]-table_ba[k][0];
					int mm=m3*1000+m2*100+m1*10+m0;
					if (mm<m && mm>=turn_time) { m=mm; k_index=k; }
				}
			}
			if (m>=turn_time && m!=2500){ sa--; b[k_index]=0; }
		}
		int *a=new int[na];
		for (j=0;j<na;j++) a[j]=1;
		for (j=0;j<nb;j++){
			int m=2500;
			int k_index;
			for (int k=0;k<na;k++){
				if (strcmp(table_bb[j],table_ab[k])!=-1 && a[k]==1){
					int m3=0; int m2=0; int m1=0; int m0=0;
					m0+=table_bb[j][4]-table_ab[k][4]; if (m0<0) { m1=-1; m0+=10; }
					m1+=table_bb[j][3]-table_ab[k][3]; if (m1<0) { m2=-1; m1+=6; }
					m2+=table_bb[j][1]-table_ab[k][1]; if (m2<0) { m3=-1; m2+=10;}
					m3+=table_bb[j][0]-table_ab[k][0];
					int mm=m3*1000+m2*100+m1*10+m0;
					if (mm<m && mm>=turn_time) { m=mm; k_index=k; }
				}
			}
			if (m>=turn_time && m!=2500){ sb--; a[k_index]=0; }
		}
		output<<"Case #"<<i+1<<": "<<sa<<' '<<sb<<endl;
	}
	input.close();
	output.close();
	return 0;
}

