#include <iostream>
#include <fstream>
#include <vector>
#define MAX_HW 10

using namespace std;




char labelBase='a';
class cell{
    public:
    int altitude;
    char label;
    vector<cell*> neighbor;
        cell(){
        label='0';
        altitude=0;
    }
    int equal(cell &another){
        if (altitude==another.altitude)
        return 1;
        else return 0;
    }
};
char Label(cell &oneCell);
//array to store the map and labels ;
cell &theLower(cell &oneCell);
int main()
{
    ifstream input;
    ofstream output;

    string inFileName,outFileName;
    cout<<"Please input the input file's location:"<<endl;
    cin>>inFileName;
    cout<<"Please input the output file's location:"<<endl;
    cin>>outFileName;
    input.open(inFileName.data());
    output.open(outFileName.data());

    int T;

    input>>T;

    for (int i=0;i<T;i++){
        labelBase='a';
        int H,W;
        input>>H>>W;
        //H:height , W:width of map;
        cell map[H][W];

        for (int j=0;j<H;j++){
            if(H==1);
            else if (j!=0){
                for (int k=0;k<W;k++)  map[j][k].neighbor.push_back(&map[j-1][k]);
            }

            for (int k=0;k<W;k++){
                input>>map[j][k].altitude;
                if (W==1);
                else if (k==0 ) {
                    map[j][k].neighbor.push_back(&map[j][k+1]);
                }
                else if (k==W-1){
                    map[j][k].neighbor.push_back(&map[j][k-1]);
                }
                else{
                    map[j][k].neighbor.push_back(&map[j][k-1]);
                    map[j][k].neighbor.push_back(&map[j][k+1]);
                }
            }
            if(H==1);
            else if (j!=H-1) {
                for (int k=0;k<W;k++)  map[j][k].neighbor.push_back(&map[j+1][k]);
            }

        }

        for (int j=0;j<H;j++){
            for (int k=0;k<W;k++){
                if (map[j][k].label=='0')
                Label(map[j][k]);
            }
        }
        output<<"Case #"<<(i+1)<<": "<<endl;
        for (int j=0;j<H;j++){
            for (int k=0;k<W;k++){
                output<<map[j][k].label<<' ';
            }
            output<<endl;
        }
    }
    input.close();
    output.close();
    cout<<"result has been saved!"<<endl;
    return 0;
}
char Label(cell &oneCell){
    if ( theLower(oneCell).equal(oneCell) ){
        if ( oneCell.label=='0'){
            oneCell.label=labelBase;
            labelBase++;
        }
        return oneCell.label;
    }
    else{
        oneCell.label=Label( theLower(oneCell) );
        return Label( theLower(oneCell) );
    }
}
cell &theLower(cell &oneCell){
    int altitudeMIN=oneCell.altitude;
    cell *LowerCell=&oneCell;
    for (int i=0;i<oneCell.neighbor.size();i++){
        if ( (*oneCell.neighbor.at(i)).altitude<altitudeMIN ){
            altitudeMIN=(*oneCell.neighbor.at(i)).altitude;
            LowerCell=oneCell.neighbor.at(i);
        }
    }
    return *LowerCell;
}
