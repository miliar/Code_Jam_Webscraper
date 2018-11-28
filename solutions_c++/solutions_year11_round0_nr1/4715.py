#include<stdio.h>

typedef struct rStatus{
    int time;
    int position;
}rStatus;

int inv(int n){
    if(n==0)
        return 1;
    return 0;
}

int abs(int n){
    if(n>0)
        return n;
    return -n;
}

int max(int a,int b){
    if(a>=b)
        return a;
    return b;
}

int main(){
    FILE* file;
    FILE* inputFile;
    file = fopen("output.out","w");
    inputFile = fopen("input.in","r");

    int T;
    fscanf(inputFile,"%d",&T);



    for(int t=0;t<T;t++){

        //�Ѻ��� N
        int N;
        fscanf(inputFile,"%d",&N);

        //૵���˹�������鹢ͧ���
        rStatus* robot = new rStatus[2];
        for(int i=0;i<2;i++){
            robot[i].position = 1;
            robot[i].time = 0;
        }

        //�����żŤ�ҷ�����Ѻ��
        for(int n=0;n<N;n++){

            //�Ѻ�������¹��
            char name;
            int robotID;
            fscanf(inputFile," %c",&name);
            if(name == 'O')
                robotID = 0;
            else
                robotID = 1;

            //�Ѻ���˹觷���ͧ��
            int target;
            fscanf(inputFile,"%d",&target);

            //��ҵ�ͨҡ������
            if(robot[robotID].time > robot[inv(robotID)].time){
                robot[robotID].time += abs(robot[robotID].position - target) + 1;
                robot[robotID].position = target;
            }else{ //�������ͨҡ������
                if((robot[robotID].time + abs(robot[robotID].position - target) + 1) > robot[inv(robotID)].time){ //������ҷ��������Թ�ҡ����
                    robot[robotID].time += abs(robot[robotID].position - target) + 1;
                    robot[robotID].position = target;
                }else{
                    robot[robotID].time = robot[inv(robotID)].time + 1;
                    robot[robotID].position = target;
                }
            }
        }

        //�ʴ���
        fprintf(file,"Case #%d: %d\n",(t+1),max(robot[0].time,robot[1].time));
    }
        fclose(file);
    return 0;
}
