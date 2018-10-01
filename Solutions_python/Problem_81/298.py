def get_WP(team_index, teams_schedule, exclude_team=None):
    if exclude_team is not None:
        team = [entry
                    for idx, entry in enumerate(teams_schedule[team_index])
                        if idx != exclude_team]
    else:
        team = teams_schedule[team_index]
    games_played = [entry for entry in team if entry != "."]
    games_won = [entry for entry in games_played if entry == "1"]
    if games_played:
        return len(games_won) / float(len(games_played))
    return 0.0

def run(teams_schedule):
    teams = {}
    for idx, entry in enumerate(teams_schedule):
        teams[idx] = {
            "WP": get_WP(idx, teams_schedule),
            }
    for idx, entry in enumerate(teams_schedule):
        opponents = [o_idx for o_idx, o_entry in enumerate(entry)
                         if o_idx != idx and o_entry != "."]
        opponents_WP = [get_WP(o_idx, teams_schedule, idx)
                            for o_idx in opponents]
        teams[idx]["opponents"] = opponents
        if opponents_WP:
            teams[idx]["OWP"] = sum(opponents_WP) / len(opponents_WP)
        else:
            teams[idx]["OWP"] = 0.0
    for idx, entry in enumerate(teams_schedule):
        o_OWPs = [teams[o_idx]["OWP"] for o_idx in teams[idx]["opponents"]]
        OOWP = sum(o_OWPs) / len(o_OWPs)
        RPI = 0.25 * teams[idx]["WP"] + 0.50 * teams[idx]["OWP"] + 0.25 * OOWP
        print RPI
    return 0

if __name__ == "__main__":
    for i in xrange(int(raw_input())):
        N = int(raw_input())
        teams_schedule = []
        for j in xrange(N):
            teams_schedule.append(raw_input())
        print "Case #%d:" % (i + 1)
        run(teams_schedule)
