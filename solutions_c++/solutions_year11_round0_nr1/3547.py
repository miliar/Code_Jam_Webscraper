#include <cstdio>
#include <cstdlib>
class robot_t {
    public:
        int last_time;
        int last_button;
        robot_t():last_time(0),last_button(1) {
        }
};
static inline int index(char robot) {
    if ('O' == robot) 
        return 0;
    else
        return 1;
}
int work() {
    robot_t* robots[2];
    robots[0] = new robot_t;
    robots[1] = new robot_t;
    int num;
    scanf("%d",&num);
    int sum = 0;
    int i;
    for (i=0; i < num; ++i) {
        char robot[2];
        int button;
        scanf("%s %d",&robot,&button);
        robot_t* robot_active = robots[index(robot[0])];
        int move = abs(button - robot_active->last_button);
        if (move + robot_active->last_time > sum) sum = move + robot_active->last_time;
        sum += 1;
        robot_active->last_button = button;
        robot_active->last_time = sum;
        //printf("i: %d, robot: %c move: %d sum: %d\n", i,robot[0],move,sum);
    }
    delete robots[0];
    delete robots[1];
    return sum;
}
int main() {
    int test;
    scanf("%d",&test);
    //printf("test is %d\n",test);
    int i;
    for (i = 0; i < test; ++i) {
        int result = work();
        printf("Case #%d: %d\n",i+1,result);
    }
    return 0;
}
