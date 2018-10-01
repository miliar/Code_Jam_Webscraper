# Saving the Universe

def read_input(input):
    num_test = int(input.readline())
    case_list = []
    
    for n in range(num_test):
        num_search = int(input.readline())
        search_list = create_list(input, num_search)
        num_query = int(input.readline())
        query_list = create_list(input, num_query)
        
        case_list.append([search_list, query_list])
        
    return case_list
        
def create_list(input, num):
    list = []
    for i in range(num):
        list.append(input.readline().strip())
    return list
            
def choose_first(search_list, query_list):
    '''
    Given lists search_list and query_list, if possible return the search engine
    that does not make an appearance in query_list, otherwise return the
    next best
    '''
    
    # Use a search engine that is not being queried at all
    for search in search_list:
        if search not in query_list:
            return search
        
    # Go through the queries until all search engines have been found
    check_list = []
    current = 0
    while len(check_list) != len(search_list):
        if query_list[current] not in check_list:
            check_list.append(query_list[current])
        current += 1
    return check_list[-1]
    
        
def count_changes(search_list, query_list):
    current = choose_first(search_list, query_list)
    if current not in query_list:
        return 0
    else:
        curr = 0
        change = 0
        while curr < len(query_list):
            if query_list[curr] == current:
                change += 1
                current = choose_first(search_list, query_list[curr:])
            curr += 1
        return change
    
def produce_output(case_list):
    order = 1
    for list in case_list:
        print "Case #" + str(order) + ": " + str(count_changes(list[0], list[1]))
        order += 1
        


if __name__ == "__main__":
    file = "A-large.in"
    file = open(file)
    case_list = read_input(file)
    produce_output(case_list)