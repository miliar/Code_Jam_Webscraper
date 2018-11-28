#include <QtCore>

QTextStream in(stdin);
QTextStream out(stdout);

int map[100][100];
int flowmap[100][100];
int H, W;
int uid;

int fillFlow(int y, int x)
{
    if(flowmap[y][x] != -1)
        return flowmap[y][x];

    int id = -1;
    int last = map[y][x];
    int cy = 0;
    int cx = 0;

    if(y+1 < H && map[y+1][x] < map[y][x]) {
        last = map[y+1][x];
        cx=0;
        cy=1;
    }

    if(x+1 < W && map[y][x+1] <= last && map[y][x+1] < map[y][x]) {
        last = map[y][x+1];
        cx=1;
        cy=0;
    }

    if(x-1 >= 0 && map[y][x-1] <= last && map[y][x-1] < map[y][x]) {
        last = map[y][x-1];
        cx=-1;
        cy=0;
    }

    if(y-1 >= 0 && map[y-1][x] <= last && map[y-1][x] < map[y][x]) {
        last = map[y-1][x];
        cx=0;
        cy=-1;
    }

    if(cx != 0 || cy != 0)
        id = fillFlow(y + cy, x + cx);

    if(id == -1)
        id = uid++;

    flowmap[y][x] = id;
    return id;
}

void printMap()
{
    char initChar = 'a';
    QMap<int, unsigned char> charMap;
    for(int i=0;i<uid;i++)
        charMap[i] = 0xFF;

    for(int y=0;y<H;y++) {
        for(int x=0;x<W;x++) {
            int id = flowmap[y][x];
            if(charMap[id] == 0xFF)
                charMap[id] = (unsigned char)(initChar++);

            if(x != 0)
                out << " ";
            out << (char)(charMap[id]);
        }
        out << endl;
    }
}

int main()
{
    int N;
    in >> N;

    for(int cas = 1; cas <= N; cas++) {
        uid = 0;
        in >> H;
        in >> W;

        for(int y=0;y<H;y++) {
            for(int x=0;x<W;x++) {
                in >> map[y][x];
                flowmap[y][x] = -1;
            }
        }


        for(int y=0;y<H;y++)
            for(int x=0;x<W;x++)
                if(flowmap[y][x] == -1)
                    fillFlow(y, x);

        out << QString("Case #%1:\n").arg(cas);
        printMap();
    }
    return 0;
}
