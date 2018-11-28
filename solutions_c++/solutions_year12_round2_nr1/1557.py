#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<cctype>
#include<cmath>
#include<map>
#include<fstream>
#include<iomanip>

using namespace std;

int main()
{
    int T;
    cin>>T;
    int P=T;
    //ofstream fout("out.txt");
    while(T--)
    {
        int N;
        cin>>N;
        vector <double> st;
        vector <double> ans;
        st.resize(N);
        ans.resize(N);
        double summ=0;
        for(int i=0;i<N;i++){
            cin>>st[i];
            summ+=st[i];
        }
        printf("Case #%d: ",P-T);
	double anssum=summ;
	int K=N;
        for(int i=0;i<N;i++){
            ans[i] = ((double)100*(2*summ*1.0 - N*st[i]))/(N*summ);
	    //cout<<ans[i];
	    if(ans[i]<0){ anssum-=st[i];ans[i]=0;K--;}
        }
	for(int i=0;i<N;i++){
		if(ans[i]!=0)
			ans[i] = ((double)100*(summ + anssum - K*st[i]))/(K*summ);
		printf("%0.6lf ",ans[i]);	
	}
        printf("\n");
    }
    return 0;
}
       



