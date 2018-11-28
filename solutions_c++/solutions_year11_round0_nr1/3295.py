#include <iostream>

#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> TIV;
typedef vector<short> TSV;

class Button {
public:
    char mColor;
    short mNumber;
    Button() : mColor(0), mNumber(0) {}
};

typedef vector<Button> TB;

class World;

class Bot{
private:
    short mPosition;
    char mColor;
    TB mMyActions;
    World &mWorld;
    short mCurrentAction;
public:
    Bot(World &inWorld, char inColor);

    bool PushButton();
};

class World {
private:
    TB mActions;
    Bot mOrange;
    Bot mBlue;
    int mTime;
    short mCurrentAction;
public:
    World(const TB& inActions) : mActions(inActions), mOrange(*this, 'O'), mBlue(*this, 'B'), mTime(0), mCurrentAction(0) {}

    const TB& GetActions() const { return mActions; }
    char GetCurrentColor() const { return mActions[mCurrentAction].mColor; }
    int GetTime() const { return mTime; }

    void Work()
    {
        while( mCurrentAction < mActions.size() ){
            bool pressed = mOrange.PushButton();
            pressed = mBlue.PushButton() || pressed;
            if(pressed) {
                mCurrentAction++;
            }
            mTime++;
        }
    }
};

Bot::Bot(World &inWorld, char inColor) : mPosition(1), mColor(inColor), mWorld(inWorld), mCurrentAction(0) {
    TB::const_iterator it(mWorld.GetActions().begin());
    for(;it!=mWorld.GetActions().end();++it) {
        if(it->mColor == mColor){
            mMyActions.push_back(*it);
        }
    }
}

bool Bot::PushButton()
{
    if(mCurrentAction < mMyActions.size()) {
        short direction = 1;
        short num = mMyActions[mCurrentAction].mNumber;

        if(mPosition > num) {
            direction = -1;
        }

        if(mPosition != num) {
            mPosition += direction;
        }
        else if(mWorld.GetCurrentColor() == mColor) {
            mCurrentAction++;
            return true;
        }
    }

    return false;
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int numCases = 0;
    in >> numCases;

    for(int c = 0; c < numCases; c++) {
        short numButtons = 0;
        in >> numButtons;

        TB actions;
        for(int b = 0; b < numButtons; b++){
            Button nb;
            in >> nb.mColor;
            in >> nb.mNumber;
            actions.push_back(nb);
        }

        World w(actions);
        w.Work();

        out << "Case #" << c + 1 << ": " << w.GetTime() << endl;
    }

    in.close();
    out.close();
    return 0;
}
