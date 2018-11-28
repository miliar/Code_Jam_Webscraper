#include <fstream.h>
const char *out_file="out.txt";
const int max=100001;
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
		int n;
		input>>n;
		int *x=new int[n];
		int *y=new int[n];
		for (int j=0;j<n;j++) input>>x[j];
		for (j=0;j<n;j++) input>>y[j];
		int *xx=order(x,n);
		int *yy=order(y,n); 
		int result=0;
		for (j=0;j<n;j++) result+=xx[j]*yy[n-1-j];
		output<<"Case #"<<i+1<<": "<<result<<endl;
	}
	input.close();
	output.close();
	return 0;
}