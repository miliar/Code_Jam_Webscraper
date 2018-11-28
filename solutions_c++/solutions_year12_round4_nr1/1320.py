#include <iostream>
#include <queue>

using namespace std;
class QueueCont{
    public:
    int x;
    int y;
    QueueCont(int, int);
};
QueueCont::QueueCont(int x, int y){
        this->x=x;
        this->y=y;
}
int main()
{
	int tests;
    int vines;
    int vl[10001];
    int vd[10001];
    int goal;
    cin >> tests;
	for(int i = 1; i<=tests; i++){
	    cin >> vines;
        for(int j = 0; j<vines; j++){
            cin >> vd[j] >> vl[j];
        }
        cin >> goal;
        vd[vines]=goal;
        vl[vines]=goal;

	    queue<QueueCont> bfs;
	    for(int j=1; j<=vines+1;j++){
            if(min(vl[0],vd[0])>=vd[j]-vd[0]){
                if(j==vines){
                    goto success;
                }
                QueueCont newNode(0,j);
                bfs.push(newNode);
            }else{
                break;
            }
	    }
	    while(!bfs.empty()){
            QueueCont node = (QueueCont)bfs.front();
            for(int j=node.y+1; j<=vines;j++){
                if(min(vl[node.y], vd[node.y]-vd[node.x])>=vd[j]-vd[node.y]){
                    if(j==vines){
                        goto success;
                    }
                    QueueCont newNode(node.y,j);
                    bfs.push(newNode);
                }else{
                    break;
                }
            }
            bfs.pop();
	    }

	    cout << "Case #"<<i<<": NO"<< endl;
        continue;

        success:
	    cout << "Case #"<<i<<": YES"<< endl;
	}
}
