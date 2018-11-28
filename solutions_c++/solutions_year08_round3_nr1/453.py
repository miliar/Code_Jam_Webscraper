#include <fstream.h>
const char *out_file="out.txt";
const int max=1000001;
int *order(const int *obj,int n)
{
	int *temp=new int[n];
	for (int i=0;i<n;i++) temp[i]=obj[i];
	int *result=new int[n];
	for (i=0;i<n;i++){
		int m=max;
		int index;
		for (int j=0;j<n;j++) if (temp[j]<m){
			m=temp[j];
			index=j;
		}
		temp[index]=max;
		result[i]=m;
	}
	return result;
}
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
	for (int i=0;i<case_num;i++){
		int p,k,l;
		input>>p>>k>>l;
		int *f=new int[l];
		for (int j=0;j<l;j++) input>>f[j];
		int *ff=order(f,l);
		double result=0;
		int t=1;
		for (j=l-1;j>=0;){
			double temp=0;
			for (int jj=0;jj<k && j-jj>=0;jj++) temp+=ff[j-jj];
			result+=temp*t;
			t++;
			j-=k;
		}
		output<<"Case #"<<i+1<<": ";
		int temp=int(result-int(result/1000000)*1000000);
		if (int(result/1000000)!=0){
			output<<int(result/1000000);
			j=1;
			temp=temp/10;
			while (temp!=0){
				j++;
				temp=temp/10;
			}
			for (int jj=0;jj<6-j;j++) output<<0;
		}
		output<<int(result-int(result/1000000)*1000000)<<endl;
	}
	input.close();
	output.close();
	return 0;
}