#include <cstdio>

struct Bot
{
    Bot(const int& position, const char& color) : Position(position), Color(color), LastTime(0){}
    int Position;
    char Color;
    int LastTime;
    int Move( int newPosition, int currentTime);
};

int Bot::Move(int newPosition, int currentTime)
{
    int time;
    int elapsedTime = currentTime - LastTime;
    int moves =  (newPosition > Position) ? (newPosition - Position) :  (Position - newPosition);

    Position = newPosition;

    time = ((moves > elapsedTime) ? (moves - elapsedTime): 0) +1;
    LastTime = currentTime + time;
    return time;
}

int main()
{    
    int t;
    int index = 1;
    unsigned long time;

#ifndef ONLINE_JUDGE
    freopen("a.in", "r", stdin);
    freopen("a.out","w", stdout);
#endif

    scanf("%d", &t);
    int numButton;
    char bot;
    int button;
    while(t--)
    {
        time = 0;
        Bot orange (1, 'O');
        Bot blue (1, 'B');
        Bot* currentBot;

        scanf("%d", &numButton);
        while(numButton--)
        {
            scanf(" %c %d", &bot, &button);
            currentBot = (bot == 'O')? &orange : &blue;
            time += currentBot->Move(button, time);
        }
        printf("Case #%d: %lu\n", index, time);
        index++;
    }

    return 0;
}
