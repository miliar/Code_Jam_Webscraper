#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

typedef enum { ON, OFF } State;

class Snapper {
    public:
        Snapper(State state = OFF, Snapper *input = NULL, Snapper *output = NULL, size_t id = (size_t)-1)
            : state(state), input(input), output(output), receiving_power(false)
        {
        }

        void AddInput(Snapper *in)
        {
            this->input = in;
            in->output = this;
        }

        void AddOutput(Snapper *out)
        {
            this->output = out;
            out->input = this;
        }

        bool& ReceivingPower() { return receiving_power; }
        bool ReceivingPower() const { return receiving_power; }

        State& SnapperState() { return state; }
        State SnapperState() const { return state; }

        friend ostream& operator<<(ostream& o, const Snapper& s);
    
        State state;
        Snapper *input;
        Snapper *output;
        bool receiving_power;
};

/**
  * ostream& operator<<(ostream& o, const Snapper& s)
  * {
  *     o << "Snapper: id = " << s.id << ", input = " << s.input->id << ", output = " << s.output->id << ", state = " << (s.state == ON ? "ON" : "OFF");
  *     return o;
  * }
  */

void SnapFingers(const vector<Snapper*>& V)
{
    vector<Snapper*> s;
    for (size_t i = 0; i < V.size(); ++i)
        s.push_back(new Snapper(*V[i]));
    for (size_t i = 1; i < s.size(); ++i)
        s[i]->AddInput(s[i-1]);

    for (size_t i = 0; i < s.size(); ++i)
    {
        if (V[i]->ReceivingPower())
            s[i]->SnapperState() = (V[i]->SnapperState() == ON) ? OFF : ON;
    }

    for (size_t i = 0; i < s.size(); ++i) {
        if (s[i]->ReceivingPower() && s[i]->SnapperState() == ON)
            s[i]->output->ReceivingPower() = true;
        else if (s[i]->SnapperState() == OFF)
            s[i]->output->ReceivingPower() = false;
    }

    for (size_t i = 0; i < s.size(); ++i) {
        V[i]->ReceivingPower() = s[i]->ReceivingPower();
        V[i]->SnapperState() = s[i]->SnapperState();
    }
}

int main(int argc, char **argv)
{
    size_t N, k, T;
    ifstream in(argv[1]);
    in >> T;

    for (size_t testnum = 1; testnum <= T; ++testnum)
    {
        in >> N >> k;
        Snapper *socket = new Snapper(ON, NULL, NULL, 200);
        socket->ReceivingPower() = true;
        Snapper *light  = new Snapper(OFF, NULL, NULL, 400);
        light->ReceivingPower() = false;
        vector<Snapper*> snappers;
        snappers.push_back(new Snapper(OFF, socket, NULL, 0));
        snappers[0]->ReceivingPower() = true;

        for (size_t i = 1; i < N; ++i) {
            Snapper *tmp = new Snapper(OFF, NULL, NULL, i);
            snappers.push_back(tmp);
            tmp->AddInput(snappers[i-1]);
        }
        light->AddInput(snappers[N-1]);

        for (size_t i = 0; i < k; ++i) {
            SnapFingers(snappers);
            if (light->input->ReceivingPower() && light->input->SnapperState() == ON)
                light->ReceivingPower() = true;
        }

        cout << "Case #" << testnum << ": " << (light->ReceivingPower() ? "ON" : "OFF") << endl;
        delete socket;
        delete light;
        for (size_t i = 0; i < snappers.size(); ++i)
            delete snappers[i];
    }
    return 0;
}
