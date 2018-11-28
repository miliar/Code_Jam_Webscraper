#include <fstream.h>
#include <string.h>
ifstream in("/Users/SunKim/Desktop/Codejam2/Untitled/p2.in");
ofstream out("/Users/SunKim/Desktop/Codejam2/Untitled/p2.out");

int main(){
	int t,c,d,n;
	int combine[27][27];
	int clear[27][27];
	char data[101];
	int visit[101];
	in >> t;
	int i,j,k;
	for(int z=0;z<t;z++){
		for(i=0;i<100;i++){
			visit[i]=0;
		}
		for(i=0;i<26;i++){
			for(j=0;j<26;j++){
				combine[i][j]=-1;
				clear[i][j]=-1;
			}
		}
		in >> c;
		for(i=0;i<c;i++){
			char temp[4];
			in >> temp;
			combine[temp[0]-'A'][temp[1]-'A']=temp[2];
			combine[temp[1]-'A'][temp[0]-'A']=temp[2];
		}
		in >> d;
		for(i=0;i<d;i++){
			char temp[3];
			in >> temp;
			clear[temp[0]-'A'][temp[1]-'A']=0;
			clear[temp[1]-'A'][temp[0]-'A']=0;
		}
		in >> n >> data;
		for(i=1;i<n;i++){
			if(combine[data[i]-'A'][data[i-1]-'A']>0 && visit[i-1]==0){
				visit[i-1]=1;
				data[i]=char(combine[data[i]-'A'][data[i-1]-'A']);
				i--;
				continue;
			}
			for(j=i-1;j>=0;j--){
				if(clear[data[i]-'A'][data[j]-'A']==0 && visit[i]==0 && visit[j]==0){
					for(k=i;k>=0;k--){
						visit[k]=1;
					}
					visit[i]=1;
					//i=j;
					break;
				}
			}
			
		}
		/*for(i=0;i<n;i++){
			for(j=i+1;j<n;j++){
				if(j-i==1){
					if(combine[data[i]-'A'][data[j]-'A']>0){
						visit[i]=1;
						data[j]=char(combine[data[i]-'A'][data[j]-'A']);
						i--;
						break;
					}else if(clear[data[i]-'A'][data[j]-'A']==0){
						visit[i]=1;
						visit[j]=1;
						i=j;
						break;
					}
				}else{
					if(clear[data[i]-'A'][data[j]-'A']==0){
						for(k=i;k<=j;k++){
							visit[k]=1;
						}
						i=j;
						break;
					}
				}
			}
		}*/
		out << "Case #" << z+1 << ": [";
		int m;
		for(i=n-1;i>=0;i--){
			if(visit[i]==0){
				m=i;
				break;
			}
		}
		for(i=0;i<n;i++){
			if(visit[i]!=1){
				out << data[i];
				if(i!=m){
					out << ", ";
				}
			}
		}
		out << "]" << "\n";
	}
	return 0;
}